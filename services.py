import os
from abc import ABC, abstractmethod
from typing import List, TypedDict, Optional

import requests
from dotenv import load_dotenv

load_dotenv(".env")


class Task(TypedDict):
    id: int
    title: str
    completed: bool


class Payload(TypedDict):
    title: Optional[str]
    completed: Optional[bool]


class ITodoService(ABC):
    @abstractmethod
    def getTasks(self) -> List[Task]:
        pass

    @abstractmethod
    def addTask(self, newTask: Task) -> Task:
        pass

    @abstractmethod
    def updateTask(self, id: int, payload: Payload) -> Task:
        pass

    @abstractmethod
    def deleteTask(self, id: int) -> None:
        pass


class TodoService(ITodoService):
    url = os.environ["URL"] + "/tasks"

    def getTasks(self) -> List[Task]:
        return requests.get(self.url).json()

    def addTask(self, newTask: Task) -> Task:
        return requests.post(self.url, data=newTask).json()

    def updateTask(self, id: int, payload: Payload) -> Task:
        return requests.patch(f"{self.url}/{id}", data=payload).json()

    def deleteTask(self, id: int) -> None:
        requests.delete(f"{self.url}/{id}")
