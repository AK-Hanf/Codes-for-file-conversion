# Metadata Management

Python codes for converting Excel and text files to JSON format with comprehensive metadata insertion templates for various analysis techniques.

## 📋 Overview

This repository contains Python utilities and metadata templates designed to streamline the process of converting data files (Excel, text) into JSON format and organizing metadata for multiple analytical characterization techniques. It serves as a centralized repository for data conversion scripts and standardized metadata collection templates.

## ✨ Features

- 🔄 **Excel to JSON Conversion** - Convert Excel files (.xlsx, .xls) to structured JSON format
- 📝 **Text to JSON Conversion** - Transform text files into JSON with proper formatting
- 🏷️ **Metadata Management** - Insert and manage metadata for converted files
- 📊 **Analysis Templates** - Pre-built metadata collection templates for 30+ characterization techniques
- 🔬 **Scientific Analysis Support** - Templates for materials science and chemistry techniques
- 📁 **Batch Processing** - Handle multiple files efficiently

## 📂 Repository Structure

```
Codes-for-file-conversion/
├── README.md                          # This file
├── codes/                             # Conversion scripts and utilities
│   ├── README.md                      # Conversion utilities documentation
│   ├── code                           # Core conversion functions
│   ├── exel to json                   # Excel to JSON converter
│   └── txt to json                    # txt to JSON converter
│
└── folder/                            # Metadata templates
    ├── README.md                      # Metadata templates guide
    ├── Metadata collection templates/ # Templates for various techniques:
    │   ├── BET.xlsx                   # Brunauer-Emmett-Teller analysis
    │   ├── CO.xlsx                    # Carbon Monoxide adsorption
    │   ├── CV.xlsx                    # Cyclic Voltammetry
    │   ├── Conductivity.xlsx          # Electrical Conductivity
    │   ├── DLS.xlsx                   # Dynamic Light Scattering
    │   ├── DRIFT.xlsx                 # Diffuse Reflectance Infrared
    │   ├── EA.xlsx                    # Elemental Analysis
    │   ├── EDX.xlsx                   # Energy Dispersive X-ray
    │   ├── EIMS.xlsx                  # Electron Impact Mass Spectrometry
    │   ├── ESIMS.xlsx                 # Electrospray Ionization MS
    │   ├── GC.xlsx                    # Gas Chromatography
    │   ├── HPLC.xlsx                  # High Performance Liquid Chromatography
    │   ├── ICP.xlsx                   # Inductively Coupled Plasma
    │   ├── IR.xlsx                    # Infrared Spectroscopy
    │   ├── NMR.xlsx                   # Nuclear Magnetic Resonance
    │   ├── PL.xlsx                    # Photoluminescence
    │   ├── PL LT.xlsx                 # Photoluminescence Low Temperature
    │   ├── PXRD.xlsx                  # Powder X-ray Diffraction
    │   ├── Raman.xlsx                 # Raman Spectroscopy
    │   ├── SEC.xlsx                   # Size Exclusion Chromatography
    │   ├── SEM.xlsx                   # Scanning Electron Microscopy
    │   ├── SXRD.xlsx                  # Single Crystal X-ray Diffraction
    │   ├── TEM.xlsx                   # Transmission Electron Microscopy
    │   ├── TG.xlsx                    # Thermogravimetric Analysis
    │   ├── TPO.xlsx                   # Temperature Programmed Oxidation
    │   ├── TPR.xlsx                   # Temperature Programmed Reduction
    │   ├── UVVis.xlsx                 # UV-Visible Spectroscopy
    │   ├── XAS.xlsx                   # X-ray Absorption Spectroscopy
    │   └── XPS.xlsx                   # X-ray Photoelectron Spectroscopy
    │
    └── synthesis and testing template/
        ├── 20250515_cat synthesis.xlsx
        └── 20250515_cat test and analytics.xlsx
```

## 🔬 Supported Analysis Techniques

The repository includes standardized metadata templates for the following characterization techniques:

### Spectroscopy Techniques
- **NMR** - Nuclear Magnetic Resonance
- **IR** - Infrared Spectroscopy
- **DRIFT** - Diffuse Reflectance Infrared Fourier Transform
- **Raman** - Raman Spectroscopy
- **UVVis** - UV-Visible Spectroscopy
- **XPS** - X-ray Photoelectron Spectroscopy
- **XAS** - X-ray Absorption Spectroscopy

### Chromatography Techniques
- **GC** - Gas Chromatography
- **HPLC** - High Performance Liquid Chromatography
- **SEC** - Size Exclusion Chromatography

### Mass Spectrometry Techniques
- **EIMS** - Electron Impact Mass Spectrometry
- **ESIMS** - Electrospray Ionization Mass Spectrometry

### Microscopy Techniques
- **SEM** - Scanning Electron Microscopy
- **TEM** - Transmission Electron Microscopy
- **EDX** - Energy Dispersive X-ray Spectroscopy

### Thermal Analysis
- **TG** - Thermogravimetric Analysis
- **TPR** - Temperature Programmed Reduction
- **TPO** - Temperature Programmed Oxidation

### Crystallography & Structural Analysis
- **PXRD** - Powder X-ray Diffraction
- **SXRD** - Single Crystal X-ray Diffraction

### Materials Characterization
- **BET** - Brunauer-Emmett-Teller (Surface Area Analysis)
- **DLS** - Dynamic Light Scattering
- **CO** - Carbon Monoxide Adsorption
- **ICP** - Inductively Coupled Plasma

### Electrochemistry
- **CV** - Cyclic Voltammetry
- **Conductivity** - Electrical Conductivity Measurements

### Photophysics
- **PL** - Photoluminescence
- **PL LT** - Photoluminescence Low Temperature

### Elemental Analysis
- **EA** - Elemental Analysis (CHN/O)

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/AK-Hanf/Codes-for-file-conversion.git
cd Codes-for-file-conversion
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

Common dependencies:
- `openpyxl` - For reading/writing Excel files
- `pandas` - For data manipulation and processing
- `json` - Built-in JSON handling
- `numpy` - Numerical computations

### Basic Usage

#### Converting Excel to JSON

```python
from codes.conversion import excel_to_json

# Convert a single Excel file
excel_to_json('input.xlsx', 'output.json')

# Convert with custom options
excel_to_json('input.xlsx', 'output.json', sheet_name='Sheet1')
```

#### Converting Text to JSON

```python
from codes.conversion import text_to_json

# Convert text file to JSON
text_to_json('input.txt', 'output.json')
```

#### Adding Metadata

```python
from codes.metadata import insert_metadata

# Insert metadata into JSON file
metadata = {
    "technique": "NMR",
    "date": "2025-05-15",
    "analyst": "Your Name",
    "instrument": "Instrument Model"
}
insert_metadata('output.json', metadata)
```

## 📊 Using Metadata Templates

1. Navigate to the `folder/` directory to access templates for each technique
2. Fill in the relevant columns with your experimental data
3. Convert the completed template to JSON using the conversion scripts
4. The resulting JSON will include all necessary metadata for data management and analysis

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Add new conversion scripts
- Create templates for additional analysis techniques
- Improve existing documentation
- Submit bug reports or enhancement requests

To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

Please see the LICENSE file (if present) for licensing information.

## ✉️ Support & Contact

For issues, questions, or suggestions, please:
- Open an issue on the [GitHub repository](https://github.com/AK-Hanf/Codes-for-file-conversion/issues)
- Review the documentation in the `codes/` and `folder/` subdirectories

---

**Created by**: AK-Hanf  
**Last Updated**: June 2026
