from pathlib import Path
import csv
import time
import argparse
import gzip


from pybgpkit_parser import Parser


DATA_FILE = Path("data/raw_data/latest-bview.gz")
#OUTPUT_FILE = Path("data/processed_data/bgp_entries.csv")
OUTPUT_FILE = Path("data/processed_data/bgp_entries.csv.gz")


PROGRESS_INTERVAL = 100_000


def iter_bgp_data(file_path):
    """
    Stream BGP entries one at a time.

    This avoids creating a huge Python list containing
    millions of BGP records in memory.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"BGP data file not found: {file_path}"
        )

    parser = Parser(url=str(file_path))

    for elem in parser:
        yield {
            "prefix": elem.prefix,
            "peer_ip": elem.peer_ip,
            "peer_asn": elem.peer_asn,
            "next_hop": elem.next_hop,
            "as_path": elem.as_path,
            "origin_asns": elem.origin_asns,
            "origin": elem.origin,
            "local_pref": elem.local_pref,
            "med": elem.med,
        }


def export_bgp_to_csv(input_file, output_file, max_entries=None):
    """
    Stream the BGP data and write it directly to CSV.

    Only a small number of records are held in memory at any time.
    """

    start_time = time.time()
    count = 0

    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("BGP DATA EXPORT")
    print("=" * 60)
    print(f"Input file : {input_file}")
    print(f"Output file: {output_file}")
    print()
    print("Starting BGP parser...")
    print()

    fieldnames = [
        "prefix",
        "peer_ip",
        "peer_asn",
        "next_hop",
        "as_path",
        "origin_asns",
        "origin",
        "local_pref",
        "med",
    ]

    with gzip.open(output_file, "wt", newline="", encoding="utf-8") as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for record in iter_bgp_data(input_file):

            writer.writerow(record)

            count += 1
            if max_entries is not None and count >= max_entries:
                break

            if count % PROGRESS_INTERVAL == 0:

                elapsed = time.time() - start_time

                rate = count / elapsed if elapsed > 0 else 0

                print(
                    f"Processed: {count:,} entries | "
                    f"Rate: {rate:,.0f} entries/sec | "
                    f"Elapsed: {elapsed:.1f} sec",
                    flush=True
                )

    elapsed = time.time() - start_time
    rate = count / elapsed if elapsed > 0 else 0

    print()
    print("=" * 60)
    print("BGP EXPORT COMPLETED")
    print("=" * 60)
    print(f"Total entries : {count:,}")
    print(f"Elapsed time  : {elapsed:.1f} seconds")
    print(f"Average rate  : {rate:,.0f} entries/sec")
    print(f"Output file   : {output_file}")
    print("=" * 60)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Export BGP MRT data to CSV"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of BGP entries to process"
    )

    args = parser.parse_args()

    export_bgp_to_csv(
        DATA_FILE,
        OUTPUT_FILE,
        max_entries=args.limit
    )

