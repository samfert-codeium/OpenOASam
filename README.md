# OpenOA

**A Python framework for wind plant operational assessment using time series data from wind plants.**

[![Journal of Open Source Software Badge](https://joss.theoj.org/papers/d635ef3c3784d49f6e81e07a0b35ff6b/status.svg)](https://joss.theoj.org/papers/d635ef3c3784d49f6e81e07a0b35ff6b)
[![PyPI version](https://badge.fury.io/py/openoa.svg)](https://badge.fury.io/py/openoa)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Documentation Badge](https://readthedocs.org/projects/openoa/badge/?version=latest)](https://openoa.readthedocs.io)
[![Code Coverage Badge](https://codecov.io/gh/NREL/OpenOA/branch/develop/graph/badge.svg)](https://codecov.io/gh/NREL/OpenOA)

<img src="https://github.com/NREL/OpenOA/blob/develop/Open%20OA%20Final%20Logos/Color/Open%20OA%20Color%20Transparent%20Background.png?raw=true" alt="OpenOA" width="300"/>

---

## Table of Contents

- [Quick Start](#quick-start)
- [What is OpenOA?](#what-is-openoa)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Analysis Methods](#analysis-methods)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Citation](#citation)

---

## Quick Start

**Try OpenOA immediately without installation:**
- 🚀 [Run example notebooks on Binder](https://mybinder.org/v2/gh/NREL/OpenOA/main?filepath=examples)

**Install and run locally:**

```bash
# Create conda environment (recommended)
conda create --name openoa-env python=3.10
conda activate openoa-env

# Install OpenOA
pip install openoa

# Verify installation
python -c "import openoa; print(f'OpenOA version: {openoa.__version__}')"
```

**Basic usage:**

```python
from openoa import PlantData
from openoa.analysis import MonteCarloAEP

# Load your wind plant data
project = PlantData.from_dict({
    "metadata": "path/to/metadata.yml",
    "scada": "path/to/scada_data.csv",
    "meter": "path/to/meter_data.csv",
    "reanalysis": {"era5": "path/to/era5_data.csv"}
})

# Run AEP analysis
aep_analysis = project.MonteCarloAEP()
aep_results = aep_analysis.run()
```

---

## What is OpenOA?

OpenOA is a software framework written in Python for assessing wind plant performance using operational assessment (OA) methodologies that consume time series data from wind plants. The goal of the project is to provide an open source implementation of common data structures, analysis methods, and utility functions relevant to wind plant OA, while providing a platform to collaborate on new functionality.

**Key Benefits:**
- 📊 **Standardized Analysis**: Implements industry-standard operational assessment methods
- 🔬 **Research-Grade**: Developed by NREL with peer-reviewed methodologies
- 🌐 **Open Source**: BSD-3 licensed for broad accessibility
- 📈 **Uncertainty Quantification**: Built-in statistical analysis and confidence intervals
- 🔧 **Extensible**: Modular design for custom analysis workflows

> **⚠️ Important Notice**  
> OpenOA is research software released under a BSD-3 license. We encourage caution, use of best practices, and engagement with subject matter experts when performing any data analysis.


---

## Key Features

### 🎯 Analysis Methods

| Method | Purpose | Key Applications |
|--------|---------|------------------|
| **MonteCarloAEP** | Long-term annual energy production estimation with uncertainty | Performance assessment, financial modeling |
| **TurbineLongTermGrossEnergy** | Turbine ideal energy calculation excluding downtime | Availability analysis, performance benchmarking |
| **WakeLosses** | Internal wake loss estimation for wind plants | Layout optimization, performance validation |
| **ElectricalLosses** | Electrical system loss quantification | Grid integration analysis |
| **EYAGapAnalysis** | Pre-construction vs. operational performance comparison | Investment validation |
| **StaticYawMisalignment** | Yaw misalignment detection and quantification | O&M optimization |

### 📋 Data Management

- **PlantData Schema**: Standardized data structure based on IEC 61400-25
- **Automated Validation**: Built-in data quality checks and validation
- **Multi-Source Integration**: SCADA, meteorological towers, revenue meters, reanalysis data
- **Flexible Import**: Support for various data formats and naming conventions

### 🛠️ Utility Functions

- **Quality Assurance**: SCADA data validation and flagging
- **Power Curve Modeling**: Advanced curve fitting and analysis
- **Data Imputation**: Missing data handling and interpolation
- **Meteorological Processing**: Air density, wind shear calculations
- **Visualization**: Publication-ready plots and plant layout maps

---

## Installation

### Requirements

- **Python**: 3.8 - 3.11
- **Operating System**: Windows, macOS, Linux
- **Package Manager**: pip (conda recommended for environment management)

### Recommended Installation

We strongly recommend using conda for environment management:

```bash
# Install Miniforge (recommended) or Miniconda
# Download from: https://github.com/conda-forge/miniforge

# Create and activate environment
conda create --name openoa-env python=3.10
conda activate openoa-env

# Install OpenOA
pip install openoa
```

### Installation Options

Install additional features as needed:

```bash
# Core installation
pip install openoa

# With example notebooks and data access
pip install "openoa[examples]"

# With development tools
pip install "openoa[develop]"

# With documentation building tools
pip install "openoa[docs]"

# Complete installation
pip install "openoa[all]"
```

### Common Installation Issues

**Windows users:**
```bash
# If you encounter geos_c.dll errors:
conda install Shapely

# If you encounter win32api errors:
pip install --upgrade pywin32==255
```

### Verify Installation

```bash
python -c "import openoa; print(f'OpenOA version: {openoa.__version__}')"
```

---

## Usage Examples

### Basic Wind Plant Analysis

```python
from openoa import PlantData
from openoa.analysis import MonteCarloAEP

# Load project data
project = PlantData.from_dict({
    "metadata": "metadata.yml",
    "scada": "scada_data.csv",
    "meter": "meter_data.csv", 
    "reanalysis": {"era5": "era5_data.csv"}
})

# Run AEP analysis
aep = project.MonteCarloAEP()
results = aep.run()

print(f"Annual Energy Production: {results.aep_GWh:.1f} GWh")
print(f"Uncertainty (P90-P10): {results.aep_GWh_P90 - results.aep_GWh_P10:.1f} GWh")
```

### Wake Loss Analysis

```python
from openoa.analysis import WakeLosses

# Analyze wake losses
wake_analysis = project.WakeLosses()
wake_results = wake_analysis.run()

print(f"Plant wake losses: {wake_results.wake_loss_total:.1%}")
```

### Data Quality Assessment

```python
from openoa.utils import qa

# Run quality checks on SCADA data
qa_results = qa.check_scada_data(project.scada)
print(f"Data availability: {qa_results.availability:.1%}")
```

---

## Analysis Methods

OpenOA implements peer-reviewed methodologies for wind plant operational assessment:

### Long-term Energy Assessment
- **MonteCarloAEP**: Estimates long-term AEP (10-20 years) from short-term data (1-3 years) with uncertainty quantification
- **TurbineLongTermGrossEnergy**: Calculates theoretical energy production excluding operational losses

### Loss Analysis
- **WakeLosses**: Quantifies internal wake effects using operational data
- **ElectricalLosses**: Measures energy losses between turbines and grid connection
- **EYAGapAnalysis**: Compares pre-construction estimates with operational performance

### Turbine Performance
- **StaticYawMisalignment**: Detects and quantifies yaw misalignment issues

> **📚 Methodology References**  
> Each analysis method is based on peer-reviewed research. See the [full documentation](https://openoa.readthedocs.io) for detailed methodology descriptions and citations.

---

## Documentation

- 📖 **[Complete Documentation](https://openoa.readthedocs.io)** - API reference, tutorials, and methodology details
- 📓 **[Example Notebooks](https://openoa.readthedocs.io/en/latest/examples)** - Interactive tutorials and use cases
- 🚀 **[Try Online](https://mybinder.org/v2/gh/NREL/OpenOA/main?filepath=examples)** - Run examples without installation
- 💬 **[Community Chat](https://gitter.im/NREL_OpenOA/community)** - Get help and discuss with other users

### Example Notebooks

- **Getting Started**: Basic PlantData usage and analysis setup
- **AEP Analysis**: Comprehensive annual energy production assessment
- **Wake Loss Analysis**: Internal wake loss quantification
- **Data Quality**: SCADA data validation and cleaning
- **Custom Analysis**: Building your own analysis workflows

---

## Contributing

We welcome contributions from the wind energy community! OpenOA is developed collaboratively to advance operational assessment methodologies.

### Quick Contribution Guide

1. **Fork** the repository on GitHub
2. **Clone** your fork locally
3. **Install** development dependencies: `pip install -e ".[develop,docs]"`
4. **Create** a feature branch: `git checkout -b feature/your-feature`
5. **Make** your changes and add tests
6. **Run** tests: `pytest --unit`
7. **Submit** a pull request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/OpenOA.git
cd OpenOA

# Install in development mode
pip install -e ".[develop,docs,examples]"

# Set up pre-commit hooks
pre-commit install

# Run tests
pytest --unit  # Fast unit tests
pytest         # All tests (may take 20+ minutes)
```

### Ways to Contribute

- 🐛 **Bug Reports**: Submit detailed issue reports
- 💡 **Feature Requests**: Propose new analysis methods or improvements
- 📝 **Documentation**: Improve guides, examples, and API documentation
- 🔬 **Research**: Contribute new validated methodologies
- 🧪 **Testing**: Add test cases and improve coverage

See our [Contributing Guide](contributing.md) for detailed guidelines.

---

## Part of the WETO Stack

OpenOA is part of the [WETO Software Stack](https://nrel.github.io/WETOStack), a comprehensive suite of wind energy tools developed by the U.S. Department of Energy.

**Related Tools:**
- [FLORIS](https://github.com/NREL/floris) - Wake modeling and wind farm controls
- [WOMBAT](https://github.com/NREL/WOMBAT) - Operations and maintenance simulation
- [WindSE](https://github.com/NREL/WindSE) - Wind farm layout optimization

---

## License

OpenOA is released under the **BSD 3-Clause License**. See [LICENSE.txt](LICENSE.txt) for full terms.

**Copyright (c) 2022, Alliance for Sustainable Energy LLC, All rights reserved.**

---

## Citation

### Citing OpenOA Software

If you use OpenOA in your research, please cite:

```bibtex
@article{Perr-Sauer2021,
   doi = {10.21105/joss.02171},
   url = {https://doi.org/10.21105/joss.02171},
   year = {2021},
   publisher = {The Open Journal},
   volume = {6},
   number = {58},
   pages = {2171},
   author = {Jordan Perr-Sauer and Mike Optis and Jason M. Fields and Nicola Bodini and Joseph C.Y. Lee and Austin Todd and Eric Simley and Robert Hammond and Caleb Phillips and Monte Lunacek and Travis Kemper and Lindy Williams and Anna Craig and Nathan Agarwal and Shawn Sheng and John Meissner},
   title = {OpenOA: An Open-Source Codebase For Operational Analysis of Wind Farms},
   journal = {Journal of Open Source Software}
}
```

### Citing Analysis Methods

When using specific analysis methods, please also cite the original research papers. See the [documentation](https://openoa.readthedocs.io) for method-specific citations.

---

## Support

- 📧 **Email**: openoa@nrel.gov
- 💬 **Chat**: [Gitter Community](https://gitter.im/NREL_OpenOA/community)
- 🐛 **Issues**: [GitHub Issues](https://github.com/NREL/OpenOA/issues)
- 📖 **Documentation**: [ReadTheDocs](https://openoa.readthedocs.io)

---

*Originally written and maintained by contributors and [Devin](https://app.devin.ai), with updates from the core team.*
