
# 🚀 GAMERA-gui : GAMERA Simulation Viewer

The **GAMERA-gui** is a python-based GUI application designed to visualize and analyze GAMERA simulation HDF5 files. It provides functionalities to load, navigate, and plot data interactively.

---

## 🌟 Features

- **📊 Interactive Visualization**: Plot and navigate through 2D projections of the simulation data.
- **🧮 Data Processing**: Automatically calculates derived quantities (e.g., Br, Btheta, Bphi) if not present in the HDF5 file.
- **📈 Time Series Analysis**: View and analyze timeseries data for selected quantities.
- **💾 Save Outputs**:
  - Save plots as PNG, JPEG, or PDF files.
  - Export animations as MP4 or GIF files.
- **⏯ Playback Controls**:
  - Navigate frames with next/previous buttons.
  - Play and pause playback.
  - Adjust playback speed.

---

## 🚀 Installation

To install and set up **GAMERA-gui**, follow these steps:

### Prerequisites
- Python 3.7 or higher
- Git
- Required Python libraries (listed in `requirements.txt`)

### Steps to install from PyPI
   ```bash
   pip install GAMERA-gui
   ```

### Steps to install from the repository

1. Clone the repository:
   ```bash
   git clone https://github.com/devojyoti96/GAMERA-gui.git
   cd GAMERA-gui
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the application:
   ```bash
   pip install ./
   ``` 
---

### Run the application
   ```bash
   gamera-gui
   ```
---

## 🛠 Usage

1. Launch the application.
2. Click on **Load HDF5 File** to select a GAMERA simulation file.
3. Choose a quantity from the dropdown menu to visualize.
4. Use the playback controls to navigate through the frames.
5. Save plots or animations using the respective buttons.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <b>Made by <a href="https://github.com/devojyoti96">Devojyoti Kansabanik</b>
</p>
