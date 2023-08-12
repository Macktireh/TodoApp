from abc import ABC
from typing import TypedDict, Optional

import requests


# Get: pour obtenir les données
# res = requests.get("http://localhost:8000/tasks")
# print("GET : ", res.json())


# Post: pour ajouter
# newTask = {'id': 6, 'title': 'Apprendre python', 'completed': False}
# res = requests.post("http://localhost:8000/tasks", data=newTask)
# print("POST : ", res.json())


# Put: pour faire une mise à jour partial
# updateTask = {'id': 6, 'title': 'Apprendre python', 'completed': True}
# res = requests.put("http://localhost:8000/tasks/6", data=updateTask)
# print(res.json())


# # Patch: pour faire une mise à jour partial
# updateTask = {'title': 'Apprendre python'}
# res = requests.patch("http://localhost:8000/tasks/6", data=updateTask)
# print(res.json())


# # delete: pour supprimer
# res = requests.delete("http://localhost:8000/tasks/6")
# print(res.json())


class ITodoService(ABC):
    def getTasks(self):
        pass

    def addTask(self, newTask):
        pass

    def updateTask(self, id, payload):
        pass

    def deleteTask(self, id):
        pass


class TaskType(TypedDict):
    id: int
    title: str
    completed: bool


class PayloadType(TypedDict):
    title: Optional[str]
    completed: Optional[bool]


class TodoService(ITodoService):
    url = "http://localhost:8000/tasks"

    def getTasks(self):
        return requests.get(self.url).json()

    def addTask(self, newTask: TaskType):
        return requests.post(self.url, data=newTask).json()

    def updateTask(self, id: int, payload: PayloadType):
        return requests.patch(f"{self.url}/{id}", data=payload).json()

    def deleteTask(self, id: int):
        return requests.post(f"{self.url}/{id}").json()
