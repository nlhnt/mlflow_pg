# Scenario 2: MLflow on localhost with SQLite
## How to run
1. `mlflow server --backend-store-uri sqlite:///db.sqlite --default-artifact-root ./mlflow_artifacts --host 0.0.0.0`  
1. `mlflow experiments list`  
1. 
## Sources:
1. https://www.mlflow.org/docs/latest/tracking.html#scenario-2-mlflow-on-localhost-with-sqlite