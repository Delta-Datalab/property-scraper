# Property Scraper

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Python Versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
![maintenance-status](https://img.shields.io/badge/maintenance-actively--developed-brightgreen.svg)
![Static Badge](https://img.shields.io/badge/release-v0.1.1-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

This Python project is a property scraper designed to extract information from various property listings available online. It utilizes web scraping techniques to collect data such as property details, prices, locations, and more from different real estate websites. The gathered data can be used for analysis, comparison, or any other purpose as required.

<img src="https://github.com/Delta-Datalab/property-scraper/blob/main/images/data_pipeline_flowchart.png">

## Project Standards

- [Git Project Standards](https://github.com/Delta-Datalab/property-scraper/blob/main/git-standards.md)
- [Code Standards](https://github.com/Delta-Datalab/property-scraper/blob/main/code-standards.md)
- [Release Standards](https://github.com/Delta-Datalab/property-scraper/blob/main/release-standards.md)

## Environment Setup

### Prerequisites

- Docker

### Installation Steps

1. Clone the repository:

``` bash
git clone https://github.com/Delta-Datalab/property-scraper.git
cd property-scraper
```

2. Build the Docker container:

``` bash
docker build -t property-scraper .
```

## Running Commands in Docker Terminal
After building the Docker container, access the container's terminal to execute project commands including setup, testing, etc.

Once inside the Docker container's terminal, the virtual environment created by Poetry is already activated and working.


### Running Tests with pytest
To run tests using the pytest framework, execute the following command:

``` bash
pytest
```