from src.text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.text_summarizer.logging import logger
from src.text_summarizer.custom_exception import CustomExeption
import sys

stage_name = 'Data Ingestion Stage'

try:
    logger.info(f'{stage_name} Started')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'{stage_name} completed')
except Exception as e:
    raise CustomExeption(e,sys)


stage_name = 'Data Validation Stage'

try:
    logger.info(f'{stage_name} Started')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'{stage_name} completed')
except Exception as e:
    raise CustomExeption(e,sys)