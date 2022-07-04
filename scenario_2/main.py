import click
import mlflow
import subprocess

cmd = """mlflow server --backend-store-uri sqlite:///db.sqlite --default-artifact-root ./mlflow_artifacts --host 0.0.0.0
"""


if __name__ == "__main__":
    p = subprocess.Popen(
        cmd.split(),
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE,
    )
    # out, err = p.communicate()
