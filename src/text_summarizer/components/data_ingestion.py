import os
import urllib.request as request
import zipfile
from src.text_summarizer.logging import logger
from src.text_summarizer.utils.common import get_size
from src.text_summarizer.custom_exception import CustomExeption
from src.text_summarizer.entity import DataIngestionConfig
from pathlib import Path
import sys

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f'{filename} downloaded! with following info: \n{headers}')

        else:
            logger.info(f'File of name {filename} already exists with size {get_size(Path(self.config.local_data_file))}')


    def extract_zip_file(self):
        ''' 
        Arg:
            zip_file_path:str

        Extracts the zip file into data directory
        Function returns none 
        '''    

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
