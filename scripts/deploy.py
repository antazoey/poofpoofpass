from ape import project
from .utils import get_account, pin_everything


def deploy():
    account = get_account(prompt="Select an account to use")
    metadata_directory_cid = pin_everything()
    account.deploy(project.PoofPoof, metadata_directory_cid)


def main():
    deploy()
