import click
from typing import Iterator, Optional

from ape import accounts, networks, config
from ape.api import AccountAPI
from ape.cli import get_user_selected_account
from ape.types import AddressType
from project_nft import NFTProject
from pynata import create_pinata, Pinata


PROJECT_NAME = "poofpoof"


def get_account(prompt: Optional[str]=None) -> AccountAPI:
    """
    Get an account. If in a development environment, returns
    ``test_accounts[0]``. Otherwise, prompts the user to select
    one of their accounts.

    Args:
        prompt (Optional[str]): The prompt to display to the user
          when selecting an account.
    
    Returns:
        ``AccountAPI``: The selected account (``ape`` class).
    """

    prompt = prompt or "Select an account"
    if get_network_name() == "development":
        return accounts.test_accounts[0]

    return get_user_selected_account(prompt_message=prompt)


def get_network_name() -> str:
    """
    Get the currently connected network name.

    Returns:
        str: The name of the network.
    """

    return networks.active_provider.network.name


def create_pinata_client() -> Pinata:
    """
    Get the client that interacts with ``pinata``.

    Returns:
        ``Pinata``
    """

    return create_pinata(PROJECT_NAME)


def pin_everything() -> str:
    """
    Pin all the artwork to IPFS via ``pinata``, including both the images
    and the metadata directory.

    Returns:
        str: The metadata directory CID from IPFS.
    """

    pinata_client = create_pinata_client()
    nft_project = NFTProject(PROJECT_NAME, pinata_client)
    content_hash_map = nft_project.pin_artwork()
    content_hashes = [f"ipfs://{cid}" for _, cid in content_hash_map.items()]
    nft_metadata_list = nft_project.create_nft_data(content_hashes)
    folder_cid = nft_project.pin_metadata(nft_metadata_list)
    return f"ipfs://{folder_cid}/"


def get_poofpoof_address() -> Optional[AddressType]:
    """
    Get the shared address of the ``PoofPoof`` smart contract
    per active network.

    Returns:
        Optional[``AddressType``]: The address of the contract in the active network.
    """

    network_name = get_network_name()
    network_deployments = config.deployments["ethereum"].get(network_name) or []
    if network_deployments:
        return [d for d in network_deployments if d["contract_type"] == "PoofPoof"][0]["address"]
    else:
        click.echo(f"No address for network '{network_name}'.", err=True)


def get_artwork_file_paths():
    return 


def get_token_receivers(token_id: int) -> Iterator[str]:
    """
    Get the address of the next token receiver
    """
    # TODO: Figure out how to populate token receivers list.
    _ = token_id
    receivers = {
        "lester": "0x4e3b9a9f52d66E62f596A7b8A258Aff9AeeB15C2"
    }
    yield from receivers.values()
