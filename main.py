from dependency_injector.wiring import Provide, inject
from dotenv import load_dotenv

from app import App
from containers import Container
from interfaces.task import ITaskService


load_dotenv(".env")


@inject
def main(taskService: ITaskService = Provide[Container.taskService]) -> None:
    App(taskService).start()


if __name__ == "__main__":
    container = Container()
    container.config.base_url.from_env("BASE_URL", required=True)
    container.wire(modules=[__name__])

    main()
