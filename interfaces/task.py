from abc import ABC, abstractmethod
from typing import List, TypedDict, Optional


class Task(TypedDict):
    id: int
    title: str
    completed: bool


class Payload(TypedDict):
    title: Optional[str]
    completed: Optional[bool]


class ITaskService(ABC):
    @abstractmethod
    def getTasks(self) -> List[Task]:
        raise NotImplementedError

    @abstractmethod
    def getTaskById(self, id: int) -> Task:
        raise NotImplementedError

    @abstractmethod
    def addTask(self, newTask: Task) -> Task:
        raise NotImplementedError

    @abstractmethod
    def updateTask(self, id: int, payload: Payload) -> Task:
        raise NotImplementedError

    @abstractmethod
    def deleteTask(self, id: int) -> None:
        raise NotImplementedError
