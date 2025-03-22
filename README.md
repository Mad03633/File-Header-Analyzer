# Development of a Method for Analyzing Main File Types Using Header Configuration Data

- Authors: Bolatov M., Dauletbay D., Tolegen M.
- Department: Intelligent Systems and Cybersecurity, Astana IT University
- Supervisor: Kalpakov Y.N.
- Date: June 2025

## Overview

This diploma project proposes a novel method for file type identification that leverages intrinsic header configuration data rather than relying solely on file extensions or metadata. The approach is designed to enhance digital forensic investigations, malware detection, and data integrity verification by:

- Extracting distinctive header properties (e.g., magic numbers, signature bytes) to accurately determine file types.
- Combining multiple analytical paradigms (statistical, textual, and visual) to increase robustness.
- Mitigating common vulnerabilities in traditional methods that rely on easily manipulated file attributes.

## Methodology

The project methodology is divided into the following key phases:

1. Data Collection:
- Aggregating header configuration data from reputable sources such as MDN Web Docs (for MIME types), HackTheMatrix (for file headers), Gary Kessler’s file signatures repository, and TrID.
- Incorporating real-world executable samples from VirusShare to validate the approach.

2. Database Creation and Integration:
- Building a PostgreSQL database populated with two primary datasets:
  - filenames.csv: Combines file header information, MIME type mappings, and signature data.
  - virusnames.csv: Contains metadata from executable samples to aid in malware detection.

3. Analytical Framework:
- Implementing a hybrid analysis approach that integrates:
  - Statistical and textual analysis to extract distinctive header features.
  - Visual analytics to enhance the interpretability of results.
- Leveraging both Python (for flexible analysis and rapid prototyping) and C++ (for performance-critical operations).

## Data Sources and Integration

The project integrates data from multiple high-quality sources to create a robust analytical framework:
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types): Provides comprehensive MIME type information.
- [HackTheMatrix](https://hackthematrixforlife.wordpress.com/file-headers/ ) & [Gary Kessler’s Repository](https://www.garykessler.net/library/file_sigs.html): Offer detailed insights into file headers and signature bytes.
- [TrID]( https://mark0.net/soft-trid-e.html): Supplies advanced binary signature identification techniques.
- [VirusShare](https://virusshare.com/): Delivers real-world executable samples for testing the reliability of the method.

## 🧠 Overview of Components

1. ⚙️ main.cpp - Header Sorter & Virus Detector

This C++ module processes two CSV files:
- ```filenames.csv```: List of filenames and their header values.
- ```virusenames.csv```: List of known malicious header patterns (signatures).

📌 Features:
- Sorts files based on header signatures.
- Detects potential viruses by checking whether any known virus signature is present in the file header (case-insensitive substring match).
- Displays a warning for any suspicious file.

2. 🔍 pe_analyzer.py — PE File Header Analyzer
