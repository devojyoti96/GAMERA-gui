from setuptools import setup

setup(
    name="GAMERA-gui",                      # Name of the package
    version="1.0.0",                       # Version
    description="GAMERA Simulation GUI", # Short description
    author="Devojyoti Kansabanik",
    author_email="dkansabanik@ucar.edu",
    py_modules=["gamera_gui"],              # The script name (without .py)
    entry_points={
        "console_scripts": [
            "gamera-gui = gamera_gui:main",  # Command-line entry point
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

