import mlflow
import numpy as np

iris_features = np.array([5.1, 3.5, 1.4, 0.2]).reshape(1, -1)

# wybieranie modelu z użyciem run_id
# run_id = "d57381a415b546f9afec8d7e2f0dfaa6"
# model_uri = f"runs:/{run_id}/random_forest_model"

# loaded_model = mlflow.pyfunc.load_model(model_uri)

# prediction = loaded_model.predict(iris_features)
# print(prediction)

# wybieranie zarejestrowanego modelu
# model_name = "IrisClassifier"
# model_version = 1
# model_uri = f"models:/{model_name}/{model_version}"

# loaded_model = mlflow.pyfunc.load_model(model_uri)

# prediction = loaded_model.predict(iris_features)
# print(prediction)

# wybieranie modelu z użyciem aliasu
model_name = "IrisClassifier"
model_uri = f"models:/{model_name}@production"

loaded_model = mlflow.pyfunc.load_model(model_uri)

prediction = loaded_model.predict(iris_features)
print(prediction)


