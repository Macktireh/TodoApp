import httpx
from dependency_injector import containers, providers

from services.taskService import TaskService


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    HTTPClient = providers.Singleton(
        httpx.Client,
        base_url=config.base_url,
    )

    taskService = providers.Factory(
        TaskService,
        HTTPClient=HTTPClient,
    )
