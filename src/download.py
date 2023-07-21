import urllib.request
from pathlib import Path

from tqdm import tqdm

from config import RAW_DATA_PATH


def download_from_cricsheet(url: str) -> Path:
    """Download cricsheet data and save to local disk."""

    file_name = url.split("/")[-1]
    file_path = RAW_DATA_PATH / file_name

    # checking whether the path exists or not
    if not Path.exists(RAW_DATA_PATH):
        Path.mkdir(RAW_DATA_PATH)

    # to avoid download again
    if Path.exists(file_path):
        return file_path

    # get total file size in bytes
    response = urllib.request.urlopen(url)
    file_size = int(response.headers["Content-Length"])

    # Download the file with a progress bar
    with tqdm(total=file_size, unit="B", unit_scale=True, unit_divisor=1024) as progress_bar:

        def progress(block_num: int, block_size: int, total_size: int):
            return progress_bar.update(block_size)

        urllib.request.urlretrieve(url, file_path, progress)

    return file_path
