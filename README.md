# BGP AI Analytics Engine

A learning and portfolio project that combines BGP routing analysis,
Python data analytics, and AI/ML techniques.

## Project Objective

Build an analytics engine capable of analyzing BGP routing data and
eventually providing intelligent network troubleshooting and
recommendation capabilities.

The long-term goal is to develop an:

> AI-powered Network Troubleshooting Assistant

that can analyze real network data such as:

- BGP routing information
- Routing tables
- Interface statistics
- NetFlow/IPFIX
- Traceroute
- Ping results
- Router configurations
- Network alarms

## Current Data Source

The initial development uses public BGP routing data from the
RIPE Routing Information Service (RIS).

The raw BGP dataset is intentionally excluded from Git because of
its large size.

## Current Capabilities

The current Python scripts can:

- Parse BGP MRT/BGPKIT data
- Extract BGP route attributes
- Display BGP prefixes
- Extract peer IP and ASN
- Extract AS paths
- Extract origin ASN
- Analyze AS-path length
- Calculate AS-path statistics
- Identify shortest and longest AS paths

## Project Structure

```text
BGP_AI_Project/
├── data/
│   ├── raw_data/
│   ├── processed_data/
│   └── output/
├── notebooks/
├── reports/
├── src/
│   ├── inspect_bgp.py
│   └── analyze_prefix.py
├── tests/
├── .gitignore
└── README.md# BGP AI Analytics Engine

A learning and portfolio project that combines BGP routing analysis,
Python data analytics, and AI/ML techniques.

## Project Objective

Build an analytics engine capable of analyzing BGP routing data and
eventually providing intelligent network troubleshooting and
recommendation capabilities.

The long-term goal is to develop an:

> AI-powered Network Troubleshooting Assistant

that can analyze real network data such as:

- BGP routing information
- Routing tables
- Interface statistics
- NetFlow/IPFIX
- Traceroute
- Ping results
- Router configurations
- Network alarms

## Current Data Source

The initial development uses public BGP routing data from the
RIPE Routing Information Service (RIS).

The raw BGP dataset is intentionally excluded from Git because of
its large size.

## Current Capabilities

The current Python scripts can:

- Parse BGP MRT/BGPKIT data
- Extract BGP route attributes
- Display BGP prefixes
- Extract peer IP and ASN
- Extract AS paths
- Extract origin ASN
- Analyze AS-path length
- Calculate AS-path statistics
- Identify shortest and longest AS paths

## Project Structure

```text
BGP_AI_Project/
├── data/
│   ├── raw_data/
│   ├── processed_data/
│   └── output/
├── notebooks/
├── reports/
├── src/
│   ├── inspect_bgp.py
│   └── analyze_prefix.py
├── tests/
├── .gitignore
└── README.md
