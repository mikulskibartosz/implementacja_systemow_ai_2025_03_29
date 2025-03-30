import bentoml
from pydantic import BaseModel
import numpy as np
import pandas as pd

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


SPECIES = {0: "setosa", 1: "versicolor", 2: "virginica"}

@bentoml.service(
    name="iris_classifier_service"
)
class IrisClassifierService:
    def __init__(self):
        self.model = bentoml.models.get("iris_classifier:latest")
        self.model = self.model.load_model()

    @bentoml.api()
    def predict(self, features: IrisFeatures):
        feature_array = np.array([
            [
                features.sepal_length,
                features.sepal_width,
                features.petal_length,
                features.petal_width
            ]
        ])
        prediction = self.model.predict(feature_array)
        species = SPECIES[prediction[0]]
        return {"species": species}

    @bentoml.api()
    def predict_batch(self, features_batch: pd.DataFrame):
        predictions = self.model.predict(features_batch)

        results = []
        for pred_class in predictions:
            species = SPECIES[pred_class]
            results.append({
                "species": species
            })
        return {"predictions": results}

