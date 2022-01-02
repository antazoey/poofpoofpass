from ape import project
from utils import get_account


def mint():
    # account = get_account(prompt="Select an account to use")
    # lester = "0x4e3b9a9f52d66E62f596A7b8A258Aff9AeeB15C2"
    contract = project.PoofPoof.at(-1)
    print(contract.address)


def main():
    mint()
