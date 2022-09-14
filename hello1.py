import prefect
from prefect import task, Flow
from datetime import timedelta
from prefect.schedules import IntervalSchedule
from prefect.storage import GitHub

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!!!")

schedule = IntervalSchedule(interval=timedelta(minutes=1))
with Flow("hello-flow11",schedule=schedule) as flow:

#with Flow("hello-flow111") as flow:
    hello_task()

flow.register(project_name="project123")

flow.storage = GitHub(
        repo="python-program",
        path="hello1.py",
	access_token_secret="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"
)


