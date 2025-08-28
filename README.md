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
![](https://github.com/Mad03633/File-Header-Analyzer/blob/main/assets/DB.jpg)

3. Analytical Framework

  - **C++**: High-performance header parsing and signature matching.

  - **Python (FastAPI)**:

      - File upload and orchestration.

      - Entropy calculation.

      - Format validation.

      - VirusTotal integration.

  - **React Frontend**: User-friendly UI for uploading files and visualizing reports.

## System Components

![Architecture](https://github.com/Mad03633/File-Header-Analyzer/blob/main/assets/architecture.jpg)

- **C++ Analyzer (cpp_analyzer)**

  - Parses binary headers from uploaded files.

  - Matches against known signatures in PostgreSQL.

  - Flags suspicious headers resembling known malware.

- **Python Analyzers**

  - entropy_analyzer.py

    - Calculates Shannon entropy.

    - Flags files with abnormal randomness as potentially packed/obfuscated.

  - signature_analyzer.py

    - Compares binary header bytes to known file type signatures.

    - Detects mismatches between extension and header.

  - validator.py

    - Validates structural integrity of common formats (PE, PDF, PNG, ZIP, ELF, MP3, etc.).

    - Flags corrupted or fake files.

  - virus_total_scanner.py

    - Computes SHA256 hash.

    - Submits file to VirusTotal API.

    - Retrieves detection stats and permalink to full report.

  - verdict_generator.py

    - Aggregates results from all analyzers.

    - Assigns final classification: Clean, Suspicious, or Malicious.

## Example Output

### Clean file

Checking the content of the file.

![](https://github.com/Mad03633/File-Header-Analyzer/blob/main/assets/cat_safe_file.jpg)

- Result:
  - ![](https://github.com/Mad03633/File-Header-Analyzer/blob/main/assets/safe_file_1.jpg)
  - ![](https://github.com/Mad03633/File-Header-Analyzer/blob/main/assets/safe_file_2.jpg)
  - ![](https://github.com/Mad03633/File-Header-Analyzer/blob/main/assets/safe_file_3.jpg)
  - ![](https://github.com/Mad03633/File-Header-Analyzer/blob/main/assets/safe_file_4.jpg)