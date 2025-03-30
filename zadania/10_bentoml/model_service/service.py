import bentoml
from pydantic import BaseModel
import pandas as pd

class PenguinFeatures(BaseModel):
    culmen_length_mm: float
    culmen_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    sex: str
    island: str

@bentoml.service(
    name="penguins_classifier_service"
)
class PenguinsClassifierService:

    def __init__(self):
        self.model = bentoml.models.get("penguins_classifier:latest").load_model()
        self.encoder = bentoml.models.get("penguins_encoder:latest").load_model()

    def _preprocess_features(self, features):
        numerical_features = pd.DataFrame({
            'culmen_length_mm': [features.culmen_length_mm],
            'culmen_depth_mm': [features.culmen_depth_mm],
            'flipper_length_mm': [features.flipper_length_mm],
            'body_mass_g': [features.body_mass_g]
        })

        categorical_features = pd.DataFrame({
            'sex': [features.sex],
            'island': [features.island]
        })

        encoded_categorical = self.encoder.transform(categorical_features)
        encoded_df = pd.DataFrame(
            encoded_categorical,
            columns=self.encoder.get_feature_names_out(['sex', 'island'])
        )

        return pd.concat([numerical_features, encoded_df], axis=1)

    def _preprocess_batch(self, features_batch):
        numerical_features = features_batch[['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g']]
        categorical_features = features_batch[['sex', 'island']]

        encoded_categorical = self.encoder.transform(categorical_features)
        encoded_df = pd.DataFrame(
            encoded_categorical,
            columns=self.encoder.get_feature_names_out(['sex', 'island']),
            index=features_batch.index
        )

        return pd.concat([numerical_features, encoded_df], axis=1)

    @bentoml.api()
    def predict(self, penguin_features: PenguinFeatures):
        """
        Przewiduje gatunek pingwina na podstawie podanych cech.
        """
        processed_features = self._preprocess_features(penguin_features)

        pred_class = self.model.predict(processed_features)

        species = pred_class[0]
        return {"species": species}

    @bentoml.api()
    def predict_batch(self, features_batch: list):
        """
        Przewiduje gatunki pingwinów dla wielu przykładów naraz.
        """
        df = pd.DataFrame(features_batch)

        processed_features = self._preprocess_batch(df)

        pred_classes = self.model.predict(processed_features)

        results = []
        for pred_class in pred_classes:
            results.append({"species": pred_class})

        return {"predictions": results}