from ape import accounts, project

from .utils import get_network_name, pin_everything


def gambit():
    assert get_network_name() == "local"
    account = accounts.load("metamask0")
    metadata_directory_cid = pin_everything()
    contract = account.deploy(project.PoofPoof, metadata_directory_cid)
    contract.safeMint(account.address, "0.json", sender=account)


def main():
    gambit()
