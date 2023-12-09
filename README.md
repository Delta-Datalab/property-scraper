# Property Scraper

This Python project is a property scraper designed to extract information from various property listings available online. It utilizes web scraping techniques to collect data such as property details, prices, locations, and more from different real estate websites. The gathered data can be used for analysis, comparison, or any other purpose as required.

<img src="https://github.com/Delta-Datalab/property-scraper/blob/main/images/data_pipeline_flowchart.png">

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