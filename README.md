# my-microglia-analysis
<img alt=”React” src= "https://img.shields.io/github/license/{jplopez19}/{my-microglia-analysis}.svg" />
<img alt=”React” src= "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />

This software package is designed to automate manual processes, create reusable functions from code, and apply efficient data-cleaning methodologies. It aims to analyze microglia cells, particularly data from the Nance Lab, providing a robust and continuous integration of new functionalities.

Overview
The main purpose of this software package is to replace hard-coded chunks of code with callable functions, thus enhancing readability, reusability, and automation. It works in tandem with other repositories from the Nance Lab, including cellmorphflows, diff_viz, microFIBER, and vampire-analysis, focusing on data cleaning, ingestion, and analysis.

The software package can be applied to different datasets but is initially designed to analyze microglia cells from the Nance Lab.

Getting Started
Clone the Repository: Clone this repository to your local machine.
Install Dependencies: Run pip install -r requirements.txt to install the necessary dependencies.
Configure Initial Path: The only manual input required is the initial path for the directory with images.
Run Main Script: Execute main.py to initiate the process.

my_software-package/
├── my_software-package (main folder)
└──
├── __init__.py
├── main.py
├── data_processing.py
├── functions.py
├── visualization.py
├── config.py
├── requirements.txt
├── README.md
├── documentation/
│   └── ...
└── tests/
    ├── test_data_processing.py
    └── …
├── notebooks/ demos (optional)


Key Components
main.py: Entry point of the package. Calls directory with images and initiates the workflow.
data_processing.py: Module for all functions related to image data processing.
functions.py: Contains reusable functions used across the project.
visualization.py: Handles plots and data visualizations.
config.py or settings.yaml: Manages configurations and parameters used across the project.
requirements.txt: Lists all project dependencies.
documentation/: Contains essential documentation files.
tests/: Holds all test files for unit and integration testing.

Testing
Tests can be found in the tests/ directory. Make sure to add your test cases incrementally as the development progresses.

Collaboration with Nance Lab
This project aligns with the goals of the Nance Lab at the University of Washington, which focuses on nanotechnology as a probe and therapeutic delivery vehicle to treat the diseased brain. Learn more about the Nance Lab.

Related Repositories
cellmorphflows: Contains Jupyter Notebooks for cell morphology quantification.
diff_viz: Enables quick data visualization for Multiple Particle Tracking (MPT).
microFIBER: Includes analysis pipelines for the microFIBER paper.
vampire-analysis: A Python package for cell and nucleus morphology quantification.
