import customtkinter as ctk

from services import TodoService


class TaskCounter:
    def __init__(self, parent) -> None:
        self.parent = parent
        self._todeService = TodoService()
        self.textLabel = ctk.StringVar(
            value=f"Tâches à faire : {len(self._todeService.getTasks())}"
        )

    def show(self):
        self.label = ctk.CTkLabel(
            self.parent,
            text=self.textLabel.get(),
            font=("arial", 25, "bold"),
            text_color=("#FFF", "#FFF"),
            fg_color="#32405b",
        ).pack(pady=15)

    def setCount(self) -> None:
        pass
