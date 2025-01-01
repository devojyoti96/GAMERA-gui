
# 🚀 GAMERA Simulation Viewer

<p align="center">
  <img src="https://via.placeholder.com/200x100.png?text=GAMERA" alt="GAMERA Logo" width="200">
</p>

The **GAMERA-gui : GAMERA Simulation Viewer** is a python-based GUI application designed to visualize and analyze GAMERA simulation HDF5 files. It provides functionalities to load, navigate, and plot data interactively.

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

## 🖼 Screenshots

<p align="center">
  <img src="https://via.placeholder.com/800x400.png?text=Screenshot+1" alt="Screenshot 1" width="80%">
</p>

<p align="center">
  <img src="https://via.placeholder.com/800x400.png?text=Screenshot+2" alt="Screenshot 2" width="80%">
</p>


---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <b>Made with ❤️ by [Devojyoti Kansabanik](https://github.com/username)</b>
</p>
