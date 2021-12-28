from pathlib import Path
from typing import Dict

from ape import project
from nft_utils import NFT
from utils import get_account, get_nft_project_manager

from scripts.utils import PROJECT_NAME

COMPLETED_ARTWORK_DIRECTORY = Path("artwork")


def create_nft(cid: str, index: int, attributes: Dict = None) -> NFT:
    # TODO: Make this more interesting / Finalize
    artwork_name = f"PoofPoof Number {index}"
    attributes = attributes or {}
    return NFT(image=cid, tokenID=index, name=artwork_name, attributes=attributes)


def main():
    # Select the account you want to use for deploying the smart contracts.
    # NOTE: We prompt for the account early to fail earlier if there is not one.
    account = get_account(prompt="Select an account to use.")

    # The NFT project manager is the bridge between IPFS and our local project.
    nft_project = get_nft_project_manager()

    # TODO: Generate the artwork and put the finishes results
    # in the COMPLETED_ARTWORK_DIRECTORY. Currently, we have a static
    # image in there as a placeholder.

    # Deploy the artwork to IPFS. NOTE: If the artwork is already deployed,
    # it will use the existing hashes.
    content_hashes = nft_project.pin_artwork(COMPLETED_ARTWORK_DIRECTORY)

    # Create the NFT metadata
    token_id = 0
    nft_data = []
    for cid in content_hashes:
        nft_metadata_dict = create_nft(cid, token_id)
        nft_data.append(nft_metadata_dict)

    # Deploy the NFT metadata to IPFS
    metadata_directory_cid = nft_project.deploy_metadata(nft_data)

    # Deploy the smart contract.
    account.deploy(project.PoofPoof, metadata_directory_cid)
