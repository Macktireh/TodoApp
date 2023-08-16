import customtkinter as ctk

from utils import countTasksNotCompleted


class TaskCounter(ctk.CTkLabel):
    def __init__(self, parent: ctk.CTk) -> None:
        self.parent = parent
        self.count = countTasksNotCompleted(self.parent.tasks)
        self.textLabel = ctk.StringVar(value=f"Tâches à faire : {self.count}")

        super().__init__(
            self.parent,
            text=self.textLabel.get(),
            font=("arial", 25, "bold"),
            text_color=("#000", "#FFF"),
        )

    def show(self) -> None:
        self.pack(pady=10)
