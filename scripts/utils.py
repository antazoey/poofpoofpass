from ape import accounts, networks
from ape.cli import get_user_selected_account


def get_account(prompt=None):
    prompt = prompt or "Select an account"
    if is_test_network():
        return accounts.test_accounts[0]

    return get_user_selected_account(prompt_message=prompt)


def is_test_network() -> bool:
    network_name = get_provider().name
    return network_name == "test"


def get_provider():
    return networks.active_provider
