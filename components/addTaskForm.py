import customtkinter as ctk


class AddTaskForm(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTk, handleAddTask: callable) -> None:
        self.parent = parent
        self.handleAddTask = handleAddTask

        super().__init__(self.parent)

        self.input = ctk.CTkEntry(
            self,
            placeholder_text="Titre",
            width=2 * self.parent.winfo_width(),
        )
        self.input.bind("<Return>", lambda event: self.addNewTask())

        self.button = ctk.CTkButton(
            self,
            command=self.addNewTask,
            text="Ajouter",
            cursor="hand2",
        )

    def show(self) -> None:
        self.pack(pady=15)
        self.input.grid(row=0, column=0, padx=10, pady=10)
        self.button.grid(row=0, column=1, padx=10, pady=10)

    def addNewTask(self) -> None:
        if self.input.get() == "":
            return
        newTask = {"title": self.input.get(), "completed": False}
        self.handleAddTask(newTask)
        self.input.delete(0, "end")
