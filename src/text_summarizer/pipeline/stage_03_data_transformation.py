from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.data_transformation import DataTransformation
from src.text_summarizer.logging import logger
from src.text_summarizer.custom_exception import CustomExeption
import sys

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise CustomExeption(e,sys)