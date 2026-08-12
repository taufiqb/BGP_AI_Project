from pybgpkit_parser import Parser
import pandas as pd

FILE_PATH = "data/latest-bview.gz"
TARGET_PREFIX = "7.0.0.0/8"

parser = Parser(url=FILE_PATH)

rows = []

for elem in parser:

    if elem.prefix != TARGET_PREFIX:
        continue

    rows.append({
        "prefix": elem.prefix,
        "peer_ip": elem.peer_ip,
        "peer_asn": elem.peer_asn,
        "next_hop": elem.next_hop,
        "as_path": elem.as_path,
        "origin_asns": elem.origin_asns,
        "origin": elem.origin,
        "local_pref": elem.local_pref,
        "med": elem.med,
    })

df = pd.DataFrame(rows)

df["as_path_length"] = df["as_path"].str.split().str.len()

print("\nNumber of BGP entries:", len(df))

print("\nDataFrame:")
print(df.to_string(index=False))

print("\nColumns:")
print(df.columns.tolist())

print("\nAS Path Length:")
print(df[["peer_asn", "as_path", "as_path_length"]].to_string(index=False))

print("\nAS Path Length Statistics:")
print(df["as_path_length"].describe())

print("\nAS Path Length Distribution:")
print(df["as_path_length"].value_counts().sort_index())


shortest = df["as_path_length"].min()

print("\nShortest AS Path Length:", shortest)

print("\nRoutes with Shortest AS Path:")
print(
    df[df["as_path_length"] == shortest]
    [["peer_ip", "peer_asn", "as_path", "as_path_length"]]
    .to_string(index=False)
)


longest = df["as_path_length"].max()

print("\nLongest AS Path Length:", longest)

print("\nRoutes with Longest AS Path:")
print(
    df[df["as_path_length"] == longest]
    [["peer_ip", "peer_asn", "as_path", "as_path_length"]]
    .to_string(index=False)
)


