from .utils import PROJECT_NAME, create_pinata_client, get_artwork_files


def clean_pins():
    client = create_pinata_client()
    directory_pin = client.get_hash(PROJECT_NAME)
    image_pins = [client.get_hash(a.name) for a in get_artwork_files()]

    client.unpin(directory_pin, ignore_errors=True)
    for pin in image_pins:
        client.unpin(pin, ignore_errors=True)


def main():
    clean_pins()
