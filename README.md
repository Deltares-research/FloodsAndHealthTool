[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# FloodsAndHealthTool

A prototype Python based tool to assess the impact of floods on human health.

# Documentation
[FloodsAndHealthTool docs](https://deltares.github.io/FloodsAndHealthTool/)

## Prerequisites

- python 3.9 or higher
- poetry 1.3 or higher ([installation instructions](https://python-poetry.org/docs/#installation))

## Install
To install the dependencies of the project create a virtual environment either with `venv` or `conda`.\
Switch to this environment and use `poetry` to restore the package dependencies.

### Create environment

#### Anaconda:

- Create `conda` environment
  ```sh
  $ conda create -y -c conda-forge --name floodshealth poetry
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