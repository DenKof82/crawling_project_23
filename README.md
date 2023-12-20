# Products Data Crawler 

## Description

Products Data Crawler is a Python script designed for web scraping and data extraction.
This script focuses on practical data extraction from e-commerce sites, particularly for
products. It utilizes Python 3, along with the `lxml`, `requests`, and `pandas` libraries. 
This project is suitable for those learning web scraping and data analysis.

## Installation

### Using a package manager

You can install the crawler as a package: Using `pip`:

```sh
pip install crawl_vitamin_c_products
```

Or using `poetry`:

```sh
poetry add crawl_vitamin_c_products
```

### Cloning the repository

You can also clone the repository and install the dependencies. Using `poetry`:

```sh
git clone https://github.com/DenKof82/crawling_project_23
cd crawling_project_23
poetry install
```

Afterwards you can checkout and run some [example](./examples) scripts, e.g.:

```sh
poetry run python examples/search?q=vitaminas+c
```

## Usage

### As a Script 

Run the script from the command line. 
It scrapes data from the specified source 
and outputs a CSV file with product data.

```python
from vitamin_c_crawler import crawl_vitamin_c_products

# Example function call
result = crawl_vitamin_c_products(
    time_limit=100,
    source="https://www.example.com/search?q=vitaminas+c",
    return_format='csv',
    download_images=True
)
print(result)
```

For more examples look in the [examples](./examples) directory.

## Structure

The project is structured as follows:

- `example_data_crawler/`: Main package directory.
  - `__init__.py`: Package initialization file.
  - `crawlers/`: Directory containing individual crawler scripts.
    - `__init__.py`: Initialization file for crawlers module.
    - `lrytas.py`: Crawler for the Lrytas website.
    - `mersedes_crawler.py`: Crawler for the Mercedes website.
  - `definitions.py`: Definitions and utility functions.
  - `dl_image.py`: Script for downloading images.
  - `main.py`: Main script for the crawler package.
- `examples/`: Directory containing example scripts.
  - `lrytas/`: Examples for the Lrytas crawlers.
    - `all.py`: Example script for crawling all data.
    - `by_topic.py`: Example script for crawling by topic.
- `tests/`: Test scripts for the package.
  - `__init__.py`: Initialization file for tests.

## License

This project is licensed under the MIT license.