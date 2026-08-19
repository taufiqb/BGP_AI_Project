# BGP AI Analytics Engine

A learning and portfolio project that combines BGP routing analysis,
Python data analytics, streaming data processing, and AI/ML techniques.

The project is being developed incrementally, starting with BGP data
analytics and progressing toward real-time network intelligence.

---

## Project Objective

Build an analytics engine capable of analyzing BGP routing data and
eventually providing intelligent network troubleshooting and
recommendation capabilities.

The long-term goal is to develop an:

> **AI-powered Network Troubleshooting Assistant**

that can analyze real network data such as:

- BGP routing information
- Routing tables
- Interface statistics
- NetFlow/IPFIX
- Traceroute
- Ping results
- Router configurations
- Network alarms

---

# Project Development Phases

## Phase 0 — Project Foundation

Establish the Python development environment, project structure,
Git repository, data directories, and initial BGP parsing capability.

### Focus

- Python environment
- Project structure
- BGP data formats
- Initial scripts
- Basic data inspection

### Status

**Completed**

---

## Phase 1 — BGP Snapshot Analytics

Phase 1 focuses on analyzing a static snapshot of public BGP routing
data.

### Data Flow

```text
Public BGP Dataset
       |
       v
     curl
       |
       v
Local BGP Snapshot
       |
       v
BGP Parser
       |
       v
Pandas DataFrame
       |
       v
BGP Analytics
```

### Data Source

The Phase 1 analysis uses public BGP routing data obtained as a
snapshot.

The raw BGP dataset is intentionally excluded from Git because of its
large size.

### Phase 1 Capabilities

The Python scripts can perform analysis including:

- Parse BGP MRT/BGPKIT data
- Extract BGP route attributes
- Display BGP prefixes
- Extract peer IP and ASN
- Extract AS paths
- Extract origin ASN
- Analyze AS-path length
- Calculate AS-path statistics
- Identify shortest and longest AS paths
- Analyze BGP route attributes
- Perform data-quality profiling
- Analyze next-hop information
- Analyze `LOCAL_PREF` availability and distribution
- Analyze route diversity

### Phase 1 Analytical Model

Phase 1 provides a point-in-time view of BGP routing information.

```text
BGP Snapshot
      |
      v
Download with curl
      |
      v
Local File
      |
      v
Parse
      |
      v
Analyze
```

### Why Phase 1 Matters

Phase 1 establishes the foundation for understanding BGP data before
moving into streaming and time-series analysis.

It is useful for:

- Reproducible analysis
- Data-quality analysis
- BGP attribute profiling
- Statistical analysis
- Batch processing
- Learning BGP data structures

### Status

**Completed / Ongoing refinement**

---

# Phase 2 — BGP Streaming Analytics

Phase 2 extends the project from static BGP snapshots to near-real-time
BGP update analysis.

Instead of downloading a BGP snapshot and analyzing it afterward,
The Phase 2 streaming experiment uses a public BGP stream provided by Route Views through BMP.

## Data Flow

```text
Public BGP Network
       |
       v
Route Views
       |
       v
Live BMP Stream
       |
       v
BGPStream
       |
       v
PyBGPStream
       |
       v
Python Streaming Engine
       |
       v
BGP Update Events
       |
       +--------------------+
       |                    |
       v                    v
Real-Time Analysis    Time-Series Data
       |                    |
       v                    v
Event Statistics      Historical Analysis
       |                    |
       +---------+----------+
                 |
                 v
          Anomaly Detection
                 |
                 v
          Network Insight
```

---

## Current Streaming Source

The current Phase 2 experiment uses:

```text
Source      : Route Views
Stream      : routeviews-stream
Data type   : BGP updates carried through BMP
Interface   : PyBGPStream
```

The `routeviews-stream` project provides access to the Route Views
live BGP stream through BGPStream.

The stream is accessed using:

```python
import pybgpstream

stream = pybgpstream.BGPStream(
    project="routeviews-stream"
)

for elem in stream:
    print(elem)
```

This is a live-stream consumption model rather than a downloaded
snapshot model.

---

# Phase 2 Environment

The Phase 2 streaming environment uses a separate native Apple
Silicon Python environment so that the Python architecture matches the
Homebrew BGPStream installation.

### Operating Environment

```text
Operating System : macOS
CPU Architecture : ARM64 / Apple Silicon
```

### Phase 1 Environment

```text
Conda environment : bgp_ai
Python            : 3.11
Architecture      : x86_64
```

### Phase 2 Environment

```text
Virtual environment : .venv_bmp
Python              : 3.11.16
Architecture        : ARM64
BGPStream           : 2.3.0
PyBGPStream         : 2.0.2
```

The Phase 1 Conda environment is kept separate from the Phase 2
environment.

This separation prevents the architecture mismatch encountered when
attempting to compile PyBGPStream against the native ARM64 BGPStream
installation from the existing x86_64 Python environment.

---

# First Successful BGP Streaming Test

The first Phase 2 live streaming test successfully connected to the
Route Views stream and received BGP update elements.

### Test Code

```python
import pybgpstream

stream = pybgpstream.BGPStream(
    project="routeviews-stream"
)

print("Connected to Route Views BMP stream")
print("Waiting for BGP updates...\n")

count = 0

for elem in stream:
    print(elem)
    count += 1

    if count >= 5:
        break

print(f"\nReceived {count} BGP elements.")
```

### Result

The test successfully produced BGP update events similar to:

```text
update|A|...|routeviews-stream|bmp-01|...
```

and completed with:

```text
Received 5 BGP elements.
```

This confirms that the Phase 2 environment can successfully consume
live BGP update events from the public Route Views stream.

---

# Snapshot vs Streaming Analytics

The project now uses two complementary BGP data acquisition models.

## Snapshot Model

The Phase 1 snapshot model provides a point-in-time view of BGP
routing information.

```text
BGP Snapshot
      |
      v
Download with curl
      |
      v
Local File
      |
      v
Parse
      |
      v
Analyze
```

This model is appropriate for:

- Point-in-time analysis
- Data profiling
- Route attribute analysis
- Statistical analysis
- Reproducible experiments

## Streaming Model

The Phase 2 streaming model continuously receives BGP update events
from a public BMP stream.

```text
BGP Updates
      |
      v
Live BMP Stream
      |
      v
PyBGPStream
      |
      v
Streaming Analytics
```

This model is appropriate for:

- Observing BGP changes over time
- Measuring update rates
- Detecting announcements
- Detecting withdrawals
- Measuring route churn
- Monitoring peer behaviour
- Building time-series datasets
- Detecting unusual routing behaviour

---

# Planned BGP Streaming Analytics

The streaming dataset will eventually be transformed into
time-series features.

## 1. BGP Update Rate

Measure the number of BGP events over time.

Examples:

- Updates / second
- Updates / minute
- Updates / hour

---

## 2. Announcements and Withdrawals

Track BGP route changes:

- Announcement
- Withdrawal
- Re-announcement

Possible time-series features include:

- `announcement_count`
- `withdrawal_count`
- `total_update_count`
- `announcement_ratio`
- `withdrawal_ratio`

---

## 3. Prefix Churn

Measure how frequently prefixes change over time.

Potential indicators include:

- New prefixes
- Withdrawn prefixes
- Re-announced prefixes
- Frequently changing prefixes

---

## 4. Peer Behaviour

Analyze BGP behaviour by peer:

- Peer IP
- Peer ASN
- Announcements
- Withdrawals
- Update rate
- Prefix diversity

This may allow normal behaviour profiles to be established for
individual BGP peers.

---

## 5. AS-Path Analysis

Analyze AS-path characteristics over time.

Potential features include:

- Average AS-path length
- Maximum AS-path length
- Minimum AS-path length
- Unique AS paths
- AS-path changes

Significant changes in AS-path behaviour may provide useful indicators
for further investigation.

---

## 6. Next-Hop Analysis

Analyze next-hop behaviour over time.

Potential indicators include:

- Unique next-hops
- Next-hop changes
- Prefixes per next-hop
- Peer / next-hop relationships

---

# Phase 2 Initial Experiment

The initial Phase 2 experiment will collect live BGP data for
increasing periods of time.

### Planned Collection Windows

```text
30 seconds
     |
     v
5 minutes
     |
     v
15 minutes
     |
     v
30 minutes
     |
     v
1 hour
```

The short experiments will be used to understand:

- Event volume
- Data format
- Update frequency
- Storage requirements
- Useful BGP attributes
- Time-series aggregation strategy

before performing longer collections.

---

# Phase 3 — Time-Series BGP Analytics

After collecting sufficient streaming data, the project will transform
individual BGP events into time-series observations.

### Conceptual Model

```text
BGP Event Stream
       |
       v
Time Window
       |
       v
Feature Aggregation
       |
       v
Time-Series Dataset
```

### Example Time-Series Dataset

```text
Timestamp
Update Count
Announcement Count
Withdrawal Count
Unique Prefixes
Unique Peers
Unique ASNs
Average AS-Path Length
Maximum AS-Path Length
Unique Next-Hops
Prefix Churn
```

This changes the analytical question from:

> "What does the BGP dataset look like?"

to:

> "What changed in the BGP network?"

---

# Phase 4 — Anomaly Detection and AI/ML

Once sufficient historical BGP time-series data has been collected,
machine-learning and anomaly-detection techniques can be introduced.

Potential applications include:

- BGP update-rate anomaly detection
- Prefix flapping detection
- Announcement spike detection
- Withdrawal spike detection
- AS-path anomaly detection
- Peer behaviour anomaly detection
- Route instability detection
- Potential route-leak indicators
- Potential route-hijack indicators

The initial approach will prioritize explainable statistical analysis
and feature engineering before introducing more complex machine
learning models.

---

# Development Philosophy

The project is intentionally developed incrementally.

```text
BGP Data
    |
    v
Data Parsing
    |
    v
Data Quality
    |
    v
Statistical Analytics
    |
    v
Streaming Analytics
    |
    v
Time-Series Analysis
    |
    v
Anomaly Detection
    |
    v
Machine Learning
    |
    v
AI Network Troubleshooting
```

The emphasis is on understanding the networking data and building the
analytics pipeline step by step before applying AI/ML techniques.

The project aims to combine practical network-engineering knowledge
with Python, data analytics, time-series analysis, and AI/ML.

---

# Long-Term Vision

The eventual architecture is:

```text
                       Network Data
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
            BGP          NetFlow         Alarms
             |              |              |
             +--------------+--------------+
                            |
                            v
                     Data Processing
                            |
                            v
                    Feature Engineering
                            |
                            v
                      Analytics / ML
                            |
                            v
                     Anomaly Detection
                            |
                            v
                    Root Cause Analysis
                            |
                            v
                  Network Recommendation
                            |
                            v
             AI Network Troubleshooting
                    Assistant
```

The long-term objective is to combine multiple network data sources
with BGP analytics and AI/ML techniques to assist network engineers
with troubleshooting, anomaly investigation, and network
recommendations.

---

# Project Structure

```text
BGP_AI_Project/
|
├── data/
│   ├── raw_data/
│   ├── processed_data/
│   └── output/
│
├── notebooks/
│
├── reports/
│
├── src/
│   ├── inspect_bgp.py
│   └── analyze_prefix.py
│
├── tests/
│
├── .venv_bmp/
│
├── .gitignore
└── README.md
```

The `.venv_bmp` directory is a local Python virtual environment and
should not be committed to Git. It should remain excluded through
`.gitignore`.

Large raw BGP datasets should also remain excluded from Git.

---

# Current Status

## Phase 0 — Project Foundation

**Status: Completed**

- Project foundation
- Python environments
- Project structure
- Initial BGP parsing

## Phase 1 — BGP Snapshot Analytics

**Status: Completed / Ongoing refinement**

- Public BGP snapshot acquisition
- BGP parsing
- Route attribute extraction
- Statistical profiling
- Data-quality analysis
- BGP route analytics

## Phase 2 — BGP Streaming Analytics

**Status: Started**

### Completed

- Native ARM64 Python 3.11 environment
- BGPStream 2.3.0 installation
- PyBGPStream 2.0.2 installation
- Route Views public streaming source
- Successful live BGP stream connection
- Successful reception of BGP update events

### Current Milestone

```text
Public Route Views BMP
          |
          v
     BGPStream 2.3.0
          |
          v
   PyBGPStream 2.0.2
          |
          v
    Python 3.11 ARM64
          |
          v
5 live BGP elements received
```

### Next Milestone

Perform controlled live-stream collections:

```text
30 seconds
     |
     v
5 minutes
     |
     v
15 minutes
     |
     v
30 minutes
     |
     v
1 hour
```

Then analyze:

- Event volume
- Announcements
- Withdrawals
- Prefix churn
- Peer behaviour
- AS-path statistics
- Next-hop behaviour
- Time-series characteristics

The results will determine the design of the longer-term BGP
streaming dataset and anomaly-detection pipeline.

---

# Git and Data Management

The project source code and documentation are tracked with Git and
GitHub.

Local virtual environments and large BGP datasets are excluded from
the repository.

Development changes should be reviewed with:

```bash
git status
git diff
```

before committing.

After a validated change:

```bash
git add .
git commit -m "Describe the change"
git push
```

The repository should contain reproducible project structure,
source code, documentation, and analysis logic without committing
large raw datasets or local Python environments.
