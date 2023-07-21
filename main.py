import logging
from pathlib import Path

from tqdm import tqdm

from config import EXTRACTED_DATA_PATH
from database import Base, engine
from src.download import download_from_cricsheet
from src.extract import extract_zip_file
from src.load import load_data_into_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CRICSHEET_DOWNLOAD_URLS = [
    "https://cricsheet.org/downloads/odis_female_json.zip",
    "https://cricsheet.org/downloads/odis_male_json.zip",
]


def main() -> None:

    # create the database
    Base.metadata.create_all(engine)

    download_path: list[Path] = []

    for url in CRICSHEET_DOWNLOAD_URLS:
        logger.info(f"Downloading {url}")
        download_path.append(download_from_cricsheet(url))

    logger.info("Download complete!")
    logger.info("Extracting files..")
    for file in download_path:
        logger.info(f"Extracting {file.name}")
        extract_zip_file(file)
    logger.info("Loading data into DB...")

    # returning the list from the generator to use in tqdm
    files = list(EXTRACTED_DATA_PATH.glob("*.json"))
    for json_file in tqdm(
        files,
        desc="Loading data into DB",
        ncols=100,
    ):
        load_data_into_db(json_file)
    logger.info("Data loaded into DB!")


if __name__ == "__main__":
    main()
