import bentoml
import mlflow
import yaml

with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

mlflow.set_tracking_uri(mlflow.get_tracking_uri())

model_name = "ChurnClassifier"

print(f"Loaded latest version of {model_name} from MLflow Model Registry")

sklearn_model = mlflow.sklearn.load_model(f"models:/{model_name}/latest")

bentoml_model_name = params.get('bento', {}).get('model_name', "churn_classifier")
bentoml_model_tag = params.get('bento', {}).get('model_tag', "latest")

bento_model = bentoml.sklearn.save_model(
    name=f"{bentoml_model_name}:{bentoml_model_tag}",
    model=sklearn_model,
    signatures={
        "predict": {"batchable": True, "batch_dim": 0},
    },
    metadata={
        "description": "Gradient Boosting Classifier for customer churn prediction",
        "source": "MLflow Registry",
        "model_name": model_name
    }
)

print(f"Model saved to BentoML: {bento_model}")
print(f"You can load this model with: bentoml.sklearn.load_model('{bento_model.tag}')")
