from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.data_validation import DataValidation
from src.text_summarizer.logging import logger
from src.text_summarizer.custom_exception import CustomExeption
import sys

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_valdation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_valdation_config)
            data_validation.validate_all_file_exists()
    
        except Exception as e:
            raise CustomExeption(e,sys)