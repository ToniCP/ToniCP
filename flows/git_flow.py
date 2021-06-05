import os
import prefect
from prefect import task, Flow
# pip install 'prefect[gitlab]'
from prefect.storage import GitHub
# pip install python-dotenv
from prefect.run_configs import LocalRun
from prefect.client.secrets import Secret
from dotenv import load_dotenv
# pip install python-decouple
from decouple import config

#load_dotenv()


@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello from prefect!")
    logger.info("Recognized repository.")
    logger.info("Accepted credentials.")


NAME_OF_FLOW = config('NAME_OF_FLOW')
with Flow('git_flow') as flow:
    say_hello()

flow.storage = GitHub(
    repo=config('REPOSITORY'),
    path=config('REPOSITORY_PATH')
)

flow.run_config = LocalRun(labels=["test"])
