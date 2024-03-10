import os
import urllib.request as request
from src.text_summarizer.logging import logger
from src.text_summarizer.utils.common import get_size
from src.text_summarizer.custom_exception import CustomExeption
from src.text_summarizer.entity import DataValidationConfig
import sys

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config

    def validate_all_file_exists(self) -> bool:
        try:
            validate_status = True

            all_file = os.listdir(os.path.join('artifacts','data_ingestion','samsum_dataset'))

            with open(self.config.STATUS_FILE,'w') as f:
                
                for file in all_file:
                    if file not in self.config.ALL_REQUIRED_FILES:
                        validate_status = False
                        f.write(f'Validation Status for {file} is {validate_status}.\n')
                    else:
                        validate_status = True
                        f.write(f'Validation Status for {file} is {validate_status}.\n')
                
            return validate_status     

        except Exception as e:
            raise CustomExeption(e,sys)