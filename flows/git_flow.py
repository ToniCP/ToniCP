import os
import prefect
from prefect import task, Flow
# pip install 'prefect[gitlab]'
from prefect.storage import GitHub
# pip install python-dotenv
from prefect.run_configs import LocalRun
from prefect.client.secrets import Secret
from dotenv import load_dotenv

load_dotenv()


@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello from prefect!")


repository_path = os.getenv('REPOSITORY_PATH')
with Flow(repository_path) as flow:
    say_hello()

flow.storage = GitHub(
    repo=os.getenv('REPOSITORY'),
    path=os.getenv('REPOSITORY_PATH')
)

flow.run_config = LocalRun(labels=["test"])
