from ape import project
from utils import get_account, pin_everything, track_deployment


def deploy():
    account = get_account(prompt="Select an account to use")
    metadata_directory_cid = pin_everything()
    contract = account.deploy(project.PoofPoof, metadata_directory_cid)
    track_deployment(contract.address)


def main():
    deploy()
