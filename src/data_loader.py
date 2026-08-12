from pathlib import Path
from pybgpkit_parser import Parser


def load_bgp_data(file_path):
    """
    Load BGP entries from a BGPStream-compatible .gz file.

    Parameters
    ----------
    file_path : str or Path
        Path to the BGP data file.

    Returns
    -------
    iterator
        Iterator containing parsed BGP elements.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"BGP data file not found: {file_path}")

    return Parser(url=str(file_path))


if __name__ == "__main__":
    data_file = "data/raw_data/latest-bview.gz"

    parser = load_bgp_data(data_file)

    first_entry = next(iter(parser))

    print("BGP data loaded successfully.")
    print(f"Entry type: {type(first_entry)}")
    print(f"Prefix: {first_entry.prefix}")
    print(f"Peer IP: {first_entry.peer_ip}")
    print(f"Peer ASN: {first_entry.peer_asn}")

