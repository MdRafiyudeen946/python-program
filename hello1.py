import prefect
from prefect import task, Flow
from datetime import timedelta
from prefect.schedules import IntervalSchedule
from prefect.storage import GitHub

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

schedule = IntervalSchedule(interval=timedelta(minutes=1))

with Flow("hello-flow1",schedule=schedule) as flow:
    hello_task()

flow.register(project_name="Project")

flow.storage = GitHub(
        repo="python-program",
        path="hello1.py"
)
