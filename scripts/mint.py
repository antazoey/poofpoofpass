from ape import project
from .utils import get_account, get_latest_poofpoof_address, get_token_receivers


def mint():
    account = get_account(prompt="Select an account to use")
    contract_address = get_latest_poofpoof_address()
    contract = project.PoofPoof.at(contract_address)

    for receiver in get_token_receivers():
        contract.safeMint(receiver, sender=account)


def main():
    mint()
