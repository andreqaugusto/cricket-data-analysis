import os
import zipfile
from pathlib import Path

from config import EXTRACTED_DATA_PATH


def extract_zip_file(file_path: Path | str) -> Path:
    """Extract a zip file to a specified destination path."""

    # just type checking
    if isinstance(file_path, Path):
        file_path = str(file_path)

    assert file_path.endswith(".zip"), "File must be a zip file."

    # Create the extracted data path if it doesn't exist
    if not os.path.exists(EXTRACTED_DATA_PATH):
        os.makedirs(EXTRACTED_DATA_PATH)

    # Open the zip file
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        # Extract all files
        zip_ref.extractall(EXTRACTED_DATA_PATH)

    return EXTRACTED_DATA_PATH
