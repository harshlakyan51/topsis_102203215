# Topsis-Harsh-102203215

**Topsis-Harsh-102203215** is a Python package for performing the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) ranking method on decision matrices. This package allows you to rank alternatives based on multiple criteria, with support for both CLI and programmatic usage. It also provides CLI functionality for processing CSV and Excel files.

## Installation

You can install the package from PyPI using pip:

```bash
pip install Topsis-Harsh-102203215
```

# Usage
CLI Usage
After installation, you can use the package directly from the command line. The general syntax for the CLI is:

topsis <input_file>  <weights>  <impacts>  <output_file>

input_file: The path to a CSV file containing the decision matrix (alternatives x criteria).

weights: A comma-separated list of weights corresponding to each criterion (e.g., 1,1,1,1).

impacts: A comma-separated list of impacts for each criterion, where + indicates a benefit and - indicates a cost (e.g., +,+, -, +).

output_file: The path where the output will be saved.


Example:
```bash
topsis input.csv "1,1,1,1" "+,+,-,+" output.csv
```

# Features

TOPSIS: Perform multi-criteria decision-making using the TOPSIS method.

CLI: Command-line interface to process decision matrices in CSV files and output rankings.

Supports CSV Files: Easily read and write decision matrices in CSV format.

# Requirements

Python 3.6 or higher
numpy >= 1.21.0
pandas >= 1.3.0

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Author

Harsh Lakyan
Email: harshlakyan@gmail.com
GitHub: https://github.com/harshlakyan51
