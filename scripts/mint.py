from ape import project

from utils import get_account, get_latest_poofpoof_address



def mint():
    account = get_account(prompt="Select an account to use")
    contract_address = get_latest_poofpoof_address()
    contract = project.PoofPoof.at(contract_address)
    contract.mint()


def main():
    mint()
