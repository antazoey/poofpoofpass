from pathlib import Path

import pytest
from nft_project import NFTProject
from pinata import create_pinata

NAME = "poofpoof"


@pytest.fixture
def pinata():
    # TODO: Make this more mocked (makes HTTP calls currently.)
    return create_pinata(NAME)


@pytest.fixture
def nft_project(pinata):
    return NFTProject(NAME, pinata)


@pytest.fixture
def artwork_path():
    return Path("artwork")


@pytest.fixture
def metadata_cid(nft_project, artwork_path):
    """NOTE: This actually makes HTTP calls"""
    content_hash_map = nft_project.pin_artwork(artwork_path)
    content_hashes = [f"ipfs://{cid}" for _, cid in content_hash_map.items()]
    nft_metadata_list = nft_project.create_nft_data(content_hashes)
    folder_cid = nft_project.pin_metadata(nft_metadata_list)
    folder_cid = f"ipfs://{folder_cid}/"
    return folder_cid


@pytest.fixture
def owner(accounts):
    return accounts[0]


@pytest.fixture
def token_receiver(accounts):
    return accounts[1]


@pytest.fixture
def poofpoof(owner, project, metadata_cid):
    return owner.deploy(project.PoofPoof, metadata_cid)
