from src.extract import Extract
import click
from config import *

import logging
import os

log_directory = os.path.dirname(LOG_DIR)
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

os.path.exists(LOG_DIR) or open(LOG_DIR, "w").close()

logging.basicConfig(
    filename=LOG_DIR,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s",
)


@click.command()
@click.argument("url")
@click.option(
    "--merge_output_data",
    "-m",
    is_flag=True,
    help="Merge the output data into a single file",
)
def main(url, merge_output_data):
    extract = Extract()
    extract.download_data(url, merge_output_data)


if __name__ == "__main__":
    main()
