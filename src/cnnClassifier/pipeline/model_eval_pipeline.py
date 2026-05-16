from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_eval_component import Evaluation
from src.cnnClassifier import logger
import os


STAGE_NAME = "Evaluation stage"




class EvaluationPipeline:
    def __init__(self):
        os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/ashwinipatil0809/itv_kidney_prediction.mlflow"
        # Set your DagsHub credentials (MLflow uses HTTP Basic Auth)
        os.environ["MLFLOW_TRACKING_USERNAME"] = "ashwinipatil0809"
        os.environ["MLFLOW_TRACKING_PASSWORD"] = "f11a94fa1604a850dc6913505b0b8699fda5b695"


    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()





