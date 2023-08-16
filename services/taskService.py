import httpx
from typing import List

from interfaces.task import ITaskService, Payload, Task


class TaskService(ITaskService):
    resource = "/tasks"

    def __init__(self, HTTPClient: httpx.Client) -> None:
        self._HTTPClient = HTTPClient

    def getTasks(self) -> List[Task]:
        return self._HTTPClient.get(self.resource).json()

    def getTaskById(self, id: int) -> Task:
        return self._HTTPClient.get(f"{self.resource}/{id}").json()

    def addTask(self, newTask: Task) -> Task:
        return self._HTTPClient.post(self.resource, data=newTask).json()

    def updateTask(self, id: int, payload: Payload) -> Task:
        return self._HTTPClient.patch(f"{self.resource}/{id}", data=payload).json()

    def deleteTask(self, id: int) -> None:
        self._HTTPClient.delete(f"{self.resource}/{id}")
