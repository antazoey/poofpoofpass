
from ape import project
from utils import get_deployment_address


def mint():
    contract_address = get_deployment_address()
    poof_poof = project.PoofPoof.at(contract_address)
    poof_poof.mint()


def main():
    mint()
