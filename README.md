[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# FloodsAndHealthTool

A prototype Python based tool to assess the impact of floods on human health.

# Documentation
[FloodsAndHealthTool docs](https://deltares.github.io/FloodsAndHealthTool/)

This script performs spatial analysis of flood and population density data in order to identify areas and exposure groups (children/adults) that are at risk of waterborne disease transmission due to flooding. The aim of the script is to show the distribution of the population in areas affected by floods, and how different flood levels are likely to affect the risk of infection with a given pathogen for different exposure groups. The infection risk and number of people in different risk classes is calculated using a Quantitative microbial risk assessment (QMRA). 

How to use the script

1.	First, ensure that all the required libraries are installed. These can be installed using the instructions below.
2.	Download the GeoTIFF/netcdf files for flood and population density data.
4.	Update the values for pathogen concentration, source, and dose-response relationship to reflect the specific pathogen for the simulation.
5.	Update the values for N50, alpha or beta to reflect the desired parameters for the Poisson distribution or exponential equation for the dose-response relationship.
6.	Pre-process the demographic data
7.	Load the flood and demographic data and create visualizations of the flood and population density data
8.	Overlay the flood and population density data to create visualizations of the areas at risk of infection due to flooding.
9.	Classify the flood data into four exposure categories based on the depth of the water.
10.	Identify the total population in each of the four categories, and calculate the percentage of the total population in each category.
11.	Use the QMRA approach to calculate the infection risk of every exposure group

Note: This script assumes that the GeoTIFF files are in the same projection and have the same spatial resolution. If the files have different projections or resolutions, additional pre-processing may be required before the analysis.

## Prerequisites

- python 3.9 or higher
- poetry 1.3 or higher ([installation instructions](https://python-poetry.org/docs/#installation))

## Dependencies

The following libraries are required for this script to run:

-matplotlib 

-tifffile 

-numpy 

-os

-netCDF4 

-rasterio 

-cartopy 

-matplotlib.colors.ListedColormap 

-matplotlib.patches 

## Install
To install the dependencies of the project create a virtual environment either with `venv` or `conda`.\
Switch to this environment and use `poetry` to restore the package dependencies.

### Create environment

#### Anaconda:

- Create `conda` environment
  ```sh
  $ conda create -y -c conda-forge --name floodshealth python=3.9 poetry 
  ```
  
- Activate `conda` environment
  ```sh
  $ conda activate floodshealth
  ```
  
### Add dependencies

```sh
$ poetry install
```

## Run

  ```sh
  $ python floodshealth/main.py
  ```

## Development

When adding a new dependency, do so using `poetry`

 - Add a new dependency
    ```sh
    $ poetry add <package>
    ```

- Add a new dependency for development
    ```sh
    $ poetry add <package> --dev
    ```

    ##test
