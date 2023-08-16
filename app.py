import customtkinter as ctk

from components.taskCounter import TaskCounter
from components.addTaskForm import AddTaskForm
from components.switchTheme import SwitchTheme
from components.taskItems import TaskItem
from interfaces.task import ITaskService, Payload, Task
from utils import countTasksNotCompleted


ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self, taskService: ITaskService) -> None:
        super().__init__()
        self.title("Todo List")
        self.geometry("700x700")
        self._taskService = taskService

        self.tasks = self._taskService.getTasks()
        self.tasks2 = self.tasks.copy()

        self.heading = ctk.CTkLabel(
            self,
            text="Application Todo List",
            font=("arial", 30, "bold"),
            text_color=("#000", "#FFF"),
        )
        self.heading.pack(pady=20)

        SwitchTheme(parent=self).show()
        TaskCounter(parent=self).show()
        AddTaskForm(parent=self, handleAddTask=self.handleAddTask).show()

        self.container = ctk.CTkScrollableFrame(
            self,
            width=620,
            height=70 * len(self.tasks),
        )
        self.container.pack(pady=10)

        for id, task in enumerate(self.tasks):
            TaskItem(
                _id=id,
                parent=self.container,
                task=task,
                handleEditTask=self.handleEditTask,
                handleDeleteTask=self.handleDeleteTask,
            ).show()

    def start(self) -> None:
        self.mainloop()

    def handleAddTask(self, payload: Task) -> None:
        newTask = self._taskService.addTask(payload)
        self.tasks.append(newTask)
        self.tasks2.append(newTask)
        TaskItem(
            _id=len(self.tasks2) - 1,
            parent=self.container,
            task=newTask,
            handleEditTask=self.handleEditTask,
            handleDeleteTask=self.handleDeleteTask,
        ).show()
        self.updateTaskCounter()

    def handleEditTask(self, id: int, payload: Payload) -> None:
        taskUpdated = self._taskService.updateTask(id, payload)
        self.tasks = list(
            map(lambda task: task if task["id"] != id else taskUpdated, self.tasks)
        )
        self.updateTaskCounter()

    def handleDeleteTask(self, id: int, name: str) -> None:
        self._taskService.deleteTask(id)
        self.container.nametowidget(name).destroy()
        self.tasks = list(filter(lambda task: task["id"] != id, self.tasks))
        self.updateTaskCounter()

    def updateTaskCounter(self) -> None:
        count = countTasksNotCompleted(self.tasks)
        self.nametowidget(".!taskcounter").configure(text=f"Tâches à faire : {count}")
