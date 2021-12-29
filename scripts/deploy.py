from pathlib import Path

from ape import project
from nft_utils import Project as NFTProject
from utils import (
    COMPLETED_ARTWORK_DIRECTORY,
    PROJECT_NAME,
    create_pinata_client,
    get_account,
    track_deployment,
)


def deploy():
    account = get_account(prompt="Select an account to use.")

    # TODO: Generate the artwork and put the finishes results
    # in the COMPLETED_ARTWORK_DIRECTORY. Currently, we have a static
    # image in there as a placeholder.

    # The NFT project manager is the bridge between IPFS and our local project.
    # TODO: Set the 'nft_data_modifier' parameter to customize the NFT metadata.
    pinata_client = create_pinata_client()
    nft_project = NFTProject(PROJECT_NAME, pinata_client)

    # Deploy the artwork to IPFS. NOTE: If the artwork is already deployed,
    # it will use the existing hashes.
    content_hashes = nft_project.pin_artwork(COMPLETED_ARTWORK_DIRECTORY)

    # Pin the metadata directory to IPFS
    nft_metadata_list = nft_project.create_nft_data(content_hashes)
    metadata_directory_cid = nft_project.pin_metadata(nft_metadata_list)

    # Deploy the smart contract.
    contract = account.deploy(project.PoofPoof, metadata_directory_cid)
    track_deployment(contract.address)


def main():
    deploy()
