from pybgpkit_parser import Parser

file_path = "data/latest-bview.gz"

parser = Parser(url=file_path)

count = 0

for elem in parser:

    if elem.prefix == "0.0.0.0/0":
        continue

    count += 1

    print(f"\n--- Route {count} ---")
    print("Prefix      :", elem.prefix)
    print("Peer IP     :", elem.peer_ip)
    print("Peer ASN    :", elem.peer_asn)
    print("Next Hop    :", elem.next_hop)
    print("AS Path     :", elem.as_path)
    print("Origin ASNs :", elem.origin_asns)
    print("Origin      :", elem.origin)
    print("Local Pref  :", elem.local_pref)
    print("MED         :", elem.med)

    if count == 5:
        break
