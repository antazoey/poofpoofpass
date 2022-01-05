from ape import project

from utils import get_latest_poofpoof_address



def mint():
    # account = get_account(prompt="Select an account to use")
    # lester = "0x4e3b9a9f52d66E62f596A7b8A258Aff9AeeB15C2"
    contract_address = get_latest_poofpoof_address()
    contract = project.PoofPoof.at(contract_address)
    print(contract.address)


def main():
    mint()
