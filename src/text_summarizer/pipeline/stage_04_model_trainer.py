import sys
from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.model_trainer import ModelTrainer
from src.text_summarizer.custom_exception import CustomExeption


class ModelTrainerTrainingPipeline():
    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_tainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise CustomExeption(e,sys)