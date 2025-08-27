# Development of a Method for Analyzing Main File Types Using Header Configuration Data

- Authors: Bolatov M., Dauletbay D., Tolegen M.
- Department: Intelligent Systems and Cybersecurity, Astana IT University
- Supervisor: Kalpakov Y.N.
- Date: June 2025

## Overview

This diploma project introduces a hybrid framework for file type identification and security analysis.
Unlike traditional methods that depend on file extensions or metadata (which are easily manipulated), our approach relies on intrinsic header configuration data and combines:

  - Signature-based identification (magic numbers, file headers).

  - Statistical entropy analysis to detect obfuscation/packing.

  - Structural validation against known format specifications.

  - Threat intelligence integration with VirusTotal for malware scanning.

Applications include digital forensics, malware detection, and data integrity verification.

## 🔬 Methodology
1. Data Collection

  - File header and MIME type data from:

    - [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types): Provides comprehensive MIME type information.
    - [HackTheMatrix](https://hackthematrixforlife.wordpress.com/file-headers/ ) & [Gary Kessler’s Repository](https://www.garykessler.net/library/file_sigs.html): Offer detailed insights into file headers and signature bytes.
    - [TrID]( https://mark0.net/soft-trid-e.html): Supplies advanced binary signature identification techniques.
    - [VirusShare](https://virusshare.com/): Delivers real-world executable samples for testing the reliability of the method.

2. Database Integration

PostgreSQL backend with primary dataset, that was collected from above sources:
[](https://github.com/Mad03633/File-Header-Analyzer/blob/main/assets/DB.jpg)

3. Analytical Framework

  - **C++**: High-performance header parsing and signature matching.

  - **Python (FastAPI)**:

      - File upload and orchestration.

      - Entropy calculation.

      - Format validation.

      - VirusTotal integration.

  - **React Frontend**: User-friendly UI for uploading files and visualizing reports.

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
