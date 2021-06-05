import os
import prefect
from prefect import task, Flow
# pip install 'prefect[gitlab]'
from prefect.storage import GitHub
# pip install python-dotenv
from prefect.run_configs import LocalRun


@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Hello from prefect!")
    logger.info("Recognized repository.")
    logger.info("Accepted credentials.")


name_of_flow = os.environ['NAME_OF_FLOW']
with Flow( name_of_flow ) as flow:
    say_hello()

flow.storage = GitHub(
    repo=os.environ['REPOSITORY'],
    path=os.environ['REPOSITORY_PATH']
)

flow.run_config = LocalRun(labels=["test"])
