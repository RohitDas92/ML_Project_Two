from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.components.model_evaluation import ModelEvaluation
from src.text_summarizer.custom_exception import CustomExeption
import sys


class ModelEvaluationTrainingPipeline():
    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_configuration()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.evaluate()
        except Exception as e:
            raise CustomExeption(e,sys)