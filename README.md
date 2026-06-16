# Codes for File Conversion

Python utilities for converting Excel spreadsheets and text files to JSON format, with support for metadata manual insertion.

## Overview

This repository contains Python scripts designed to simplify data conversion workflows, specifically focusing on converting Excel files and text files to JSON format. These utilities are particularly useful for data management, research data workflows, and data processing pipelines.

## Features

- **Excel to JSON Conversion**: Convert Excel sheets to JSON format with proper null/NaN handling
- **Text to JSON Conversion**: Convert text files to JSON format
- **Metadata Support**: Designed to facilitate manual metadata insertion
- **Error Handling**: Robust error handling for file operations
- **UTF-8 Encoding**: Proper Unicode support for international characters

## Project Structure

```
codes/
├── code                    # Text file to JSON conversion script
├── exel to json           # Excel to JSON conversion script
└── codes                  # Supporting files
```

## Scripts

### 1. Excel to JSON Conversion (`exel to json`)

Converts Excel spreadsheets to JSON format.

**Features:**
- Reads specified Excel sheet
- Converts to list of dictionaries (records format)
- Handles NaN values (converts to `null` in JSON)
- UTF-8 encoding support
- Comprehensive error messages

**Dependencies:**
- `pandas`
- `json` (built-in)

**Usage:**
```python
from exel_to_json import excel_sheet_to_json

excel_path = r"C:\path\to\your\file.xlsx"
sheet_name = "Sheet1"
json_path = r"C:\path\to\output.json"

excel_sheet_to_json(excel_path, sheet_name, json_path)
```

**Example:**
```python
excel_sheet_to_json(
    excel_path=r"C:\Users\Ankit\Desktop\data.xlsx",
    sheet_name="Sheet1",
    json_path=r"C:\Users\Ankit\Desktop\data.json"
)
```

### 2. Text to JSON Conversion (`code`)

Converts text files to JSON format (one line per JSON array element).

**Features:**
- Reads text file line by line
- Skips empty lines
- Converts to JSON array format
- UTF-8 encoding support
- Auto-naming of output files

**Dependencies:**
- `json` (built-in)
- `os` (built-in)

**Usage:**
```python
from code import txt_to_json

# Auto-name output file (same name, .json extension)
txt_to_json(r"path\to\your\file.txt")

# Or specify custom output path
txt_to_json(r"path\to\input.txt", r"path\to\output.json")
```

**Example:**
```python
txt_to_json(r"Y:\working group\Arjun\Research Data Management\Data-Panda\all\MS\THF+la_cu_3h_neg.txt")
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AK-Hanf/Codes-for-file-conversion.git
cd Codes-for-file-conversion
```

2. Install required dependencies:
```bash
pip install pandas
```

3. Use the scripts in your Python projects or run them directly

## Requirements

- Python 3.6+
- `pandas` (for Excel conversion)

## Usage Examples

### Convert Excel to JSON

```python
import sys
sys.path.insert(0, 'codes')
from excel_to_json import excel_sheet_to_json

# Convert a specific sheet
excel_sheet_to_json(
    excel_path="data.xlsx",
    sheet_name="Employees",
    json_path="employees.json"
)
```

### Convert Text to JSON

```python
import sys
sys.path.insert(0, 'codes')
from code import txt_to_json

# Convert with auto-naming
txt_to_json("data.txt")

# Convert with custom output path
txt_to_json("data.txt", "data.json")
```

## Output Format

### Excel to JSON Output
```json
[
    {
        "Name": "John Doe",
        "Age": 30,
        "Department": "Engineering",
        "Salary": null
    },
    {
        "Name": "Jane Smith",
        "Age": 28,
        "Department": "Marketing",
        "Salary": 75000
    }
]
```

### Text to JSON Output
```json
[
    "Line 1 content",
    "Line 2 content",
    "Line 3 content"
]
```

## Error Handling

Both scripts include error handling for common issues:

- **FileNotFoundError**: When input file doesn't exist
- **ValueError**: When specified sheet name doesn't exist (Excel conversion)
- **Generic Exception**: For other unexpected errors

## Metadata Manual Insertion

After conversion, you can easily add or modify metadata in the generated JSON files using any text editor or programmatically:

```python
import json

# Load generated JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Add metadata
metadata = {
    "source": "original_file.xlsx",
    "conversion_date": "2024-01-15",
    "converted_by": "data_team"
}

output = {
    "metadata": metadata,
    "data": data
}

# Save with metadata
with open("data_with_metadata.json", "w") as f:
    json.dump(output, f, indent=4)
```

## License

This project is provided as-is for data conversion and research purposes.

## Contributing

Feel free to submit issues and enhancement requests!

## Contact

For questions or suggestions, please open an issue in the repository.

---

**Note:** Always ensure you have proper backups of your data before running conversion scripts. Test with sample data first.
