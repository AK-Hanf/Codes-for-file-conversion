# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 11:59:41 2025

@author: Arbeit
"""

import pandas as pd
import json
import os

def excel_sheet_to_nested_json(df, json_output_path):
    """
    Converts a single pandas DataFrame into a nested JSON file.
    """
    try:
        # Initialize the nested JSON structure
        json_data = {
            "General_information": {},
            "Device": {},
            "sample preparation": {},
            "Sample pretreatment": {},
            "size-exclusion chromatography": {}
        }
        
        # Define the mapping of Excel keys to their nested JSON location
        key_map = {
            "sample name": "General_information",
            "sample state": "General_information",
            "sample description": "General_information",
            "Analytics ID": "General_information",
            "institution": "General_information",
            "characterization technique": "General_information",
            "equipment": "Device",
            "detector type": "Device",
            "sample holder": "sample preparation",
            "particle size": "sample preparation",
            "pretreatment vessel type": "Sample pretreatment",
            "pretreatment atmosphere": "Sample pretreatment",
            "pretreatment flow rate": "Sample pretreatment",
            "pretreatment duration": "Sample pretreatment",
            "pretreatment temperature": "Sample pretreatment",
            "pretreatment heating procedure": "Sample pretreatment",
            "column type": "size-exclusion chromatography",
            "Eluent": "size-exclusion chromatography",
            "Calibration standard": "size-exclusion chromatography",
            "Temperature": "size-exclusion chromatography",
            "Flow rate": "size-exclusion chromatography",
            "injection volume setting": "size-exclusion chromatography"
        }
        
        # Iterate through the DataFrame rows to populate the JSON structure
        for index, row in df.iterrows():
            key = str(row['key']).strip()
            value = str(row['value']).strip()
            
            if key in key_map:
                parent_key = key_map[key]
                json_data[parent_key][key] = value
        
        # Ensure the output directory exists
        output_dir = os.path.dirname(json_output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")
        
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)
            
        print(f"Successfully converted sheet to JSON. Output saved to: {json_output_path}")

    except Exception as e:
        print(f"An error occurred while processing the sheet: {e}")

# --- Main execution logic for multiple sheets ---
excel_file_path = r"C:\Users\Arbeit\Desktop\learntocode\Carbodiol Characterisation\SEC.xlsx"
output_folder = r"C:\Users\Arbeit\Desktop\learntocode\Carbodiol Characterisation\json_outputs_SEC"

try:
    # Read all sheets from the Excel file into a dictionary of DataFrames
    all_sheets = pd.read_excel(excel_file_path, sheet_name=None, header=None, names=["key", "value"])

    for sheet_name, df in all_sheets.items():
        print(f"\nProcessing sheet: '{sheet_name}'")

        # Extract the value for "Analytics ID" from the current sheet's DataFrame
        analytics_id = None
        try:
            analytics_id_row = df[df['key'] == 'Analytics ID']
            if not analytics_id_row.empty:
                analytics_id = str(analytics_id_row['value'].iloc[0]).strip()
        except Exception as e:
            pass

        # Determine the filename for this sheet's JSON output
        output_json_filename = ""
        if analytics_id and analytics_id.lower() not in ('nan', 'id'):
            output_json_filename = f"metadata_{analytics_id}.json"
        else:
            print("No valid 'Analytics ID' found for this sheet. Using sheet name as filename.")
            output_json_filename = f"metadata_{sheet_name}.json"
        
        # Construct the full output path
        json_output_path = os.path.join(output_folder, output_json_filename)

        # Run the conversion for the current sheet
        excel_sheet_to_nested_json(df, json_output_path)

except FileNotFoundError:
    print(f"Error: The file '{excel_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")