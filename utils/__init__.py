from typing import List

from interfaces.task import Task


def booleanUtiles(value: bool | str) -> bool:
    if type(value) == bool:
        return value
    return value == "true"


def countTasksNotCompleted(tasks: List[Task]) -> int:
    return len(list(filter(lambda task: not booleanUtiles(task["completed"]), tasks)))
