from src.text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.text_summarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.text_summarizer.logging import logger
from src.text_summarizer.custom_exception import CustomExeption
import sys

stage_name = 'Data Ingestion Stage'

try:
    logger.info(f'{stage_name} Started')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'{stage_name} Completed')
except Exception as e:
    raise CustomExeption(e,sys)


stage_name = 'Data Validation Stage'

try:
    logger.info(f'{stage_name} Started')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'{stage_name} Completed')
except Exception as e:
    raise CustomExeption(e,sys)

stage_name = 'Data Transformation Stage'

try:
    logger.info(f'{stage_name} Started')
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f'{stage_name} Completed')
except Exception as e:
    raise CustomExeption(e,sys)


stage_name = 'Data Transformation Stage'

try:
    logger.info(f'{stage_name} Started')
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f'{stage_name} Completed')
except Exception as e:
    raise CustomExeption(e,sys)
