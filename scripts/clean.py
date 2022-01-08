import json
from json.decoder import JSONDecodeError

from utils import (
    get_artwork_file_paths,
    DEPLOYMENT_MAP_PATH,
    PROJECT_NAME,
    create_pinata_client,
)


def clean_pins():
    client = create_pinata_client()
    directory_pin = client.get_hash(PROJECT_NAME)
    image_pins = [
        client.get_hash(p.name) for p in get_artwork_file_paths()
    ]

    client.unpin(directory_pin, ignore_errors=True)
    for pin in image_pins:
        client.unpin(pin, ignore_errors=True)


def clean_testnet_deployments():
    if DEPLOYMENT_MAP_PATH.exists():
        with open(DEPLOYMENT_MAP_PATH, "r") as map_file:
            try:
                map_dict = json.load(map_file)
            except JSONDecodeError:
                map_dict = {}
    else:
        return

    map_dict["rinkeby"] = []
    map_dict["kovan"] = []
    map_dict["goerli"] = []
    map_dict["ropsten"] = []

    DEPLOYMENT_MAP_PATH.unlink()
    with open(DEPLOYMENT_MAP_PATH, "w") as map_file:
        json.dump(map_dict, map_file)


def main():
    clean_pins()
    clean_testnet_deployments()
