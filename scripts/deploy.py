from ape import project
from .utils import get_account


def main():
    account = get_account(prompt="Select an account to deploy 'PoofPoof.sol'")
    account.deploy(project.Fund)
