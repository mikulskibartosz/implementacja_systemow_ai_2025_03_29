Kolejność poleceń:

```bash
dvc init --subdir

dvc stage add -n download_data -d download.py -o data/x_train.csv -o data/y_train.csv -o data/x_test.csv -o data/y_test.csv python download.py

dvc repro

dvc stage add -n train -d train.py -d params.yaml -d data/x_train.csv -d data/y_train.csv -d data/x_test.csv -d data/y_test.csv python train.py

dvc stage add -n make_bento -d make_bento.py -d params.yaml python make_bento.py

dvc repro

cd model_service
bentoml build
bentoml containerize churn_classifier_service:latest

docker run --rm -d -p 3000:3000 churn_classifier_service:...

curl -X 'POST' 'http://localhost:3000/predict' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"churn_features": {"CreditScore": 300, "Age": 42, "Tenure": 2, "Balance": 4000, "NumOfProducts": 1, "HasCrCard": 0, "IsActiveMember": 1, "EstimatedSalary": 30000, "Geography_France": true, "Geography_Germany": false, "Geography_Spain": false, "Gender_Female": true, "Gender_Male": false}}'

docker ps

docker stop <container_id>
```

