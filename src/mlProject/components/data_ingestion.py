import os
import urllib.request as request
import zipfile
import logger # type: ignore
from mlProject.utils.common import get_size
from pathlib import Path
from src.mlProject.entity.config_entity import DataIngestionConfig

class DataIngestionConfig:
    def __init__(self, root_dir, source_URL, local_data_file, unzip_dir):
        self.root_dir = root_dir
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir

    def download_file(self):
        if not os.path.exists(self.local_data_file):
            try:
                filename, headers = request.urlretrieve(
                    url=self.source_URL,
                    filename=self.local_data_file
                )
                logger.info(f"{filename} downloaded with the following info:\n{headers}")
            except Exception as e:
                logger.error(f"Error downloading file: {e}")
        else:
            logger.info(f"File already exists: {self.local_data_file}")

    def extract_zip_file(self):
        try:
            unzip_path = self.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Zip file extracted to: {unzip_path}")
        except Exception as e:
            logger.error(f"Error extracting zip file: {e}")

if __name__ == "__main__":
    try:
        # Create an instance of DataIngestionConfig with your configuration
        data_ingestion = DataIngestionConfig(
            root_dir="artifacts",
            source_URL="https://github.com/Mayu21ad/dataset/raw/main/wine_quality.zip",
            local_data_file="artifacts/data_ingestion/data.zip",
            unzip_dir="artifacts/data_ingestion"
        )

        # Download and extract the file
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    except Exception as e:
        logger.error(f"Error: {e}")
