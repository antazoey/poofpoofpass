from ape import project
from utils import get_account, get_deployment_address


def mint():
    account = get_account(prompt="Select an account to use")
    lester = "0x4e3b9a9f52d66E62f596A7b8A258Aff9AeeB15C2"

    contract_address = get_deployment_address()
    poof_poof = project.PoofPoof.at(contract_address)

    poof_poof.safeMint(lester, "0", sender=account)


def main():
    mint()
