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


STORAGE = GitHub(
    repo=os.getenv('REPOSITORY'),
    path=os.getenv('PATH')
)

with Flow(os.getenv('NAME_OF_FLOW_1'), storage=STORAGE,
          run_config=LocalRun(labels=["test"])) as flow:
    say_hello()
