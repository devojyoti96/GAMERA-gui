# README

## GAMERA Simulation Viewer

The **GAMERA Simulation Viewer** is a PyQt5-based GUI application designed to visualize and analyze GAMERA simulation HDF5 files. It provides functionalities to load, navigate, and plot data interactively.

---

### Features
- **Interactive Visualization**: Plot and navigate through 2D projections of the simulation data.
- **Data Processing**: Automatically calculates derived quantities (e.g., Br, Btheta, Bphi) if not present in the HDF5 file.
- **Time Series Analysis**: View and analyze timeseries data for selected quantities.
- **Save Outputs**:
  - Save plots as PNG, JPEG, or PDF files.
  - Export animations as MP4 or GIF files.
- **Playback Controls**:
  - Navigate frames with next/previous buttons.
  - Play and pause playback.
  - Adjust playback speed.

---

### Installation

#### Prerequisites
- Python 3.7 or later
- Required Python packages:
  - `numpy`
  - `h5py`
  - `matplotlib`
  - `PyQt5`
  - `astropy`

#### Steps
1. Clone the repository or download the script.
2. Install the required dependencies:
   ```bash
   pip install numpy h5py matplotlib PyQt5 astropy
   ```
3. Run the application:
   ```bash
   python my_script.py
   ```

---

### Usage

1. Launch the application.
2. Click on **Load HDF5 File** to select a GAMERA simulation file.
3. Choose a quantity from the dropdown menu to visualize.
4. Use the playback controls to navigate through the frames.
5. Save plots or animations using the respective buttons.

---

### License
This project is licensed under the MIT License. See the LICENSE file for details.

---

### Acknowledgments
This application utilizes PyQt5 for the GUI and matplotlib for visualization. Special thanks to the developers of these libraries for making this project possible.
