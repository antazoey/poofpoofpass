from ape import accounts, networks
from ape.api import AccountAPI, ProviderAPI
from ape.cli import get_user_selected_account
from nft_utils import Project as NFTProject
from pynata import create_pinata

PROJECT_NAME = "poofpoof"


def get_account(prompt=None) -> AccountAPI:
    prompt = prompt or "Select an account"
    if is_development():
        return accounts.test_accounts[0]

    return get_user_selected_account(prompt_message=prompt)


def is_development() -> bool:
    return get_provider().network.name == "development"


def get_provider() -> ProviderAPI:
    return networks.active_provider


def get_nft_project_manager() -> NFTProject:
    pinata = create_pinata(PROJECT_NAME)
    return NFTProject(pinata)
