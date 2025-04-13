import bentoml
from pydantic import BaseModel
import pandas as pd

class ChurnFeatures(BaseModel):
    CreditScore: int
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    Geography_France: bool
    Geography_Germany: bool
    Geography_Spain: bool
    Gender_Female: bool
    Gender_Male: bool

@bentoml.service(
    name="churn_classifier_service"
)
class ChurnClassifierService:

    def __init__(self):
        self.model = bentoml.models.get("churn_classifier:gradient_boosting").load_model()

    @bentoml.api()
    def predict(self, churn_features: ChurnFeatures):
        """
        Przewiduje czy klient odejdzie (churn) na podstawie podanych cech.
        """

        churn_features_dict = churn_features.dict()
        churn_features_df = pd.DataFrame([churn_features_dict])

        pred_class = self.model.predict(churn_features_df)

        exited = int(pred_class[0])
        return {"exited": exited}

    @bentoml.api()
    def predict_batch(self, features_batch: list):
        """
        Przewiduje churn dla wielu klientów naraz.
        """
        df = pd.DataFrame(features_batch)

        pred_classes = self.model.predict(df)

        results = []
        for pred_class in pred_classes:
            results.append({"exited": int(pred_class)})

        return {"predictions": results}