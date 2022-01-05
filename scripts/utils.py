import click
import json
from pathlib import Path
from typing import Dict, Optional

from ape import accounts, networks, config
from ape.api import AccountAPI
from ape.cli import get_user_selected_account
from ape.types import AddressType
from nft_utils import Project as NFTProject
from pynata import create_pinata


PROJECT_NAME = "poofpoof"
DEPLOYMENT_MAP_PATH = Path("deployment_map.json")
COMPLETED_ARTWORK_DIRECTORY = Path("artwork")


def get_account(prompt=None) -> AccountAPI:
    prompt = prompt or "Select an account"
    if get_network_name() == "development":
        return accounts.test_accounts[0]

    return get_user_selected_account(prompt_message=prompt)


def get_network_name() -> str:
    return networks.active_provider.network.name


def get_deployment_map() -> Dict:
    map_json_file = DEPLOYMENT_MAP_PATH
    if map_json_file.exists():
        with open(map_json_file, "r") as json_file:
            return json.load(json_file)

    return {}


def create_pinata_client():
    return create_pinata(PROJECT_NAME)


def pin_everything() -> str:
    pinata_client = create_pinata_client()
    nft_project = NFTProject(PROJECT_NAME, pinata_client)
    content_hash_map = nft_project.pin_artwork(COMPLETED_ARTWORK_DIRECTORY)
    content_hashes = [f"ipfs://{cid}" for _, cid in content_hash_map.items()]
    nft_metadata_list = nft_project.create_nft_data(content_hashes)
    folder_cid = nft_project.pin_metadata(nft_metadata_list)
    return f"ipfs://{folder_cid}/"


def get_latest_poofpoof_address() -> Optional[AddressType]:
    network_name = get_network_name()
    network_deployments = config.deployments["ethereum"].get(network_name) or []
    if network_deployments:
        return [d for d in network_deployments if d["contract_type"] == "PoofPoof"][0]["address"]
    else:
        click.echo(f"No address for network '{network_name}'.")
        return None
