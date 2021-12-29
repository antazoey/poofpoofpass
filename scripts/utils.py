import json
from pathlib import Path
from typing import Dict, Optional

from ape import accounts, networks
from ape.api import AccountAPI
from ape.cli import get_user_selected_account
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


# TODO: Replace this once https://github.com/ApeWorX/ape/issues/374 is done.
def track_deployment(contract_address: str):
    current_network = get_network_name()

    if current_network == "development":
        # We don't track development deployments.
        return

    map_json = get_deployment_map()

    if current_network in map_json:
        map_json[current_network].append(contract_address)
    else:
        map_json[current_network] = [contract_address]

    if DEPLOYMENT_MAP_PATH.exists():
        DEPLOYMENT_MAP_PATH.unlink()

    with open(str(DEPLOYMENT_MAP_PATH), "w") as json_file:
        json.dump(map_json, json_file)


def create_pinata_client():
    return create_pinata(PROJECT_NAME)


def get_deployment_address() -> Optional[str]:
    with open(DEPLOYMENT_MAP_PATH, "r") as map_file:
        map_data = json.load(map_file)
    
    network = get_network_name()
    deployments = map_data.get(network, [])
    if deployments:
        return deployments[-1]
