# Property Scraper

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Python Versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
![Not Maintained](https://img.shields.io/badge/Maintenance%20Level-Not%20Maintained-yellow.svg)
![Static Badge](https://img.shields.io/badge/release-v0.2.0-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

This Python project is a property scraper designed to extract information from various property listings available online. It utilizes web scraping techniques to collect data such as property details, prices, locations, and more from different real estate websites. The gathered data can be used for analysis, comparison, or any other purpose as required.

<img src="https://github.com/Delta-Datalab/property-scraper/blob/main/images/data_pipeline_flowchart.png">

## Table of Contents

- [Results](#results)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [API Documentation](#api-documentation)
  - [Endpoints](#endpoints)
    - [Get Locations](#get-locations)
    - [Filter Properties](#filter-properties)
    - [Get New Properties](#get-new-properties)
- [Project Standards](#project-standards)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
  - [Running Tests](#running-tests)
- [Future Work](#future-work)
- [License](#license)

## Results

After more than a month of data collection, we've observed significant trends in the real estate market that we visualized with Looker:

- **Increase in Property Listings**: There is a noticeable upward trend in the number of properties listed in both U.S. dollars and Argentine pesos. This suggests growing activity in the property market, and could be attributed to recent government regulations that have stimulated demand.

  <p align="center">
    <img src="https://github.com/Delta-Datalab/property-scraper/blob/main/images/offers-by-currency.png">

  
- **Rising Median Prices**: The median price of properties has increased throughout the month. This could be attributed to inflation impacting property valuations.

These trends provide valuable insights for investors, real estate professionals, and economists interested in understanding market dynamics in Argentina.

To see a deep dive into our analisis follow this link: [https://lookerstudio.google.com/s/ksmw_VJSu_I](https://lookerstudio.google.com/reporting/4c83e752-d604-46f9-92d8-70b983a5fd30)

## Features

- **Comprehensive Data Extraction**: Scrapes property details including prices, locations, and descriptions.
- **RESTful API**: Provides an API to access and query the scraped data.
- **Market Trend Analysis**: Enables analysis of property listing trends and price movements over time.
- **Multi-Site Support**: Provides a structure that follows the Open/Close principle for scraping data from multiple real estate websites.
- **Data Export**: Exports collected data in various formats such as CSV and JSON.
- **Easy Setup**: Simple setup using Docker and Poetry for dependency management.
- **Automated Testing**: Includes a suite of tests using pytest to ensure code reliability.

## API Documentation

The Property Scraper provides a RESTful API to access the scraped property data. Below are the available endpoints and their usage.

### Endpoints

#### Get Locations

- **URL:** `/locations`
- **Method:** `GET`
- **Description:** Retrieves a list of distinct property locations.

#### Filter Properties

- **URL:** `/properties/filter`
- **Method:** `GET`
- **Description:** Retrieves properties based on provided filter criteria.
- **Query Parameters:**
  - **`location`** *(optional)*: Filter by property location.
  - **`min_price`** *(optional)*: Minimum property price.
  - **`max_price`** *(optional)*: Maximum property price.
  - **`property_type`** *(optional)*: Type of property (e.g., apartment, house).
  - *Additional filters as supported by the application.*

#### Get New Properties

- **URL:** `/properties/new/<provided_date>`
- **Method:** `GET`
- **Description:** Retrieves properties uploaded on the provided date that were not available the day before.
- **URL Parameters:**
  - **`provided_date`** *(required)*: Date in `YYYY-MM-DD` format.
  
## Project Standards

- [Git Project Standards](https://github.com/Delta-Datalab/property-scraper/blob/main/standards/git-standards.md)
- [Code Standards](https://github.com/Delta-Datalab/property-scraper/blob/main/standards/code-standards.md)
- [Release Standards](https://github.com/Delta-Datalab/property-scraper/blob/main/standards/release-standards.md)


## Installation

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)

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

After building the Docker container, access the container's terminal to execute project commands including setup, testing, etc.

Once inside the Docker container's terminal, the virtual environment created by Poetry is already activated and working.

### Running Tests
To run tests using the pytest framework, execute the following command:

``` bash
pytest
```

## Future Work

We would like to enhance the Property Scraper project with the following features:

- **Advanced Data Analytics**: Incorporate machine learning models to predict property price trends.
- **Geospatial Analysis**: Visualize property data on interactive maps for better geographical insights.
- **User Interface**: Develop a web-based dashboard to display real-time analytics and trends.
- **Additional Data Sources**: Expand scraping capabilities to include more real estate websites for a broader dataset.
- **Automated Alerts**: Implement a notification system for significant market changes or user-defined criteria.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
