# Codes - Data Conversion Utilities

This folder contains Python scripts for converting experimental data from Excel format to JSON, enabling seamless integration with databases and analysis pipelines.

## Overview

The codes in this folder provide utilities to automate the conversion of analytical data stored in Excel spreadsheets into JSON format, which is ideal for:
- Database storage and retrieval
- API integration
- Data analysis and visualization
- Cross-platform data sharing

## Contents

### Scripts

#### **exel to json**
A Python utility for converting Excel sheets to JSON format.

**Features:**
- Converts single Excel sheets to JSON files
- Handles NaN values and converts them to JSON `null`
- Preserves data types during conversion
- UTF-8 encoding support for international characters
- Includes error handling for common issues (missing files, invalid sheet names)

**Usage:**
```python
from exel_to_json import excel_sheet_to_json

# Define file paths and sheet name
excel_path = "path/to/your/file.xlsx"
sheet_name = "Sheet1"
json_path = "path/to/output/file.json"

# Convert Excel sheet to JSON
excel_sheet_to_json(excel_path, sheet_name, json_path)
```

**Parameters:**
- `excel_path` (str): Full path to the source Excel file
- `sheet_name` (str): Name of the Excel sheet to convert
- `json_path` (str): Full path where the JSON output file will be saved

**Example:**
```python
excel_sheet_to_json(
    r"C:\data\analytical_results.xlsx",
    "Spectroscopy_Data",
    r"C:\data\spectroscopy_output.json"
)
```

## Requirements

### Dependencies
- **pandas** - For reading and manipulating Excel data
- **openpyxl** or **xlrd** - Required by pandas for Excel file support

### Installation

```bash
# Install required packages
pip install pandas openpyxl
```

## Usage Workflow

1. **Prepare your data** - Organize experimental data in Excel using the standardized templates from the `folder/` directory
2. **Run the conversion script** - Use `excel_sheet_to_json()` function to convert the data
3. **Validate JSON output** - Check the generated JSON file for completeness and accuracy
4. **Integrate with database** - Use the JSON output for database insertion or API calls

## Example Workflow

```python
import pandas as pd
import json
from exel_to_json import excel_sheet_to_json

# Convert XPS spectroscopy data
excel_sheet_to_json(
    "analytical_data/spectroscopy.xlsx",
    "XPS",
    "json_output/xps_data.json"
)

# Convert HPLC chromatography data
excel_sheet_to_json(
    "analytical_data/chromatography.xlsx",
    "HPLC",
    "json_output/hplc_data.json"
)
```

## Data Format

### Input (Excel)
Excel sheets should be organized with:
- **Header row** - Column names describing the data
- **Data rows** - Experimental measurements and metadata

Example:
| Sample_ID | Temperature (°C) | Pressure (atm) | Yield (%) |
|-----------|-----------------|----------------|-----------|
| S001      | 25.0            | 1.0            | 87.5      |
| S002      | 50.0            | 1.5            | 92.3      |

### Output (JSON)
Each row becomes a JSON object with column names as keys:

```json
[
    {
        "Sample_ID": "S001",
        "Temperature (°C)": 25.0,
        "Pressure (atm)": 1.0,
        "Yield (%)": 87.5
    },
    {
        "Sample_ID": "S002",
        "Temperature (°C)": 50.0,
        "Pressure (atm)": 1.5,
        "Yield (%)": 92.3
    }
]
```

## Features

- ✅ Automatic NaN handling (converts to JSON `null`)
- ✅ Preserves data types (integers, floats, strings, etc.)
- ✅ UTF-8 encoding for special characters
- ✅ Error handling with informative messages
- ✅ Pretty-printed JSON output (4-space indentation)
- ✅ Command-line executable for standalone use

## Error Handling

The script includes built-in error handling for:
- **FileNotFoundError** - Excel file path is incorrect or file doesn't exist
- **ValueError** - Sheet name doesn't exist in the Excel file
- **General exceptions** - Other unexpected errors during conversion

## Related Files

- See `folder/` for Excel templates for different analytical techniques
- See repository root for main documentation and additional tools

## Contributing

When adding new conversion utilities:
1. Follow the existing code style and structure
2. Include comprehensive docstrings
3. Add error handling for common issues
4. Update this README with usage examples

## License

See the repository LICENSE file for details.

## Support

For issues or questions:
1. Check the example usage above
2. Verify Excel file and sheet names match exactly
3. Ensure all dependencies are installed (`pip install -r requirements.txt`)
4. Review the error messages provided by the script

---

**Last Updated:** 2025-06-16
