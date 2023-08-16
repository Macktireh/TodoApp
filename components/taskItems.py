import customtkinter as ctk
from PIL import Image

from interfaces.task import Task
from utils import booleanUtiles


class TaskItem(ctk.CTkFrame):
    def __init__(
        self,
        _id: int,
        parent: ctk.CTkScrollableFrame,
        task: Task,
        handleEditTask: callable,
        handleDeleteTask: callable,
    ) -> None:
        self._id = _id
        self.parent = parent
        self.task = task
        self.handleEditTask = handleEditTask
        self.handleDeleteTask = handleDeleteTask
        self.isEditing = False

        super().__init__(self.parent, width=610, height=50)

        self.checkboxValue = ctk.BooleanVar(value=booleanUtiles(self.task["completed"]))
        self.checkbox = ctk.CTkCheckBox(
            self,
            command=self.updateTaskCompleted,
            text="",
            variable=self.checkboxValue,
            cursor="hand2",
            onvalue=True,
            offvalue=False,
            width=50,
        )

        self.label = ctk.CTkLabel(
            self,
            text=self.task["title"],
            font=("arial", 18, "bold"),
            width=430,
            justify=ctk.LEFT,
            anchor=ctk.NW,
        )

        self.boxInput = ctk.CTkFrame(self, width=430)
        self.entryValue = ctk.StringVar(value=self.task["title"])
        self.input = ctk.CTkEntry(
            self.boxInput,
            textvariable=self.entryValue,
            placeholder_text="Titre",
            width=self.boxInput.winfo_reqwidth() - self.boxInput.winfo_reqwidth() // 3,
        )
        self.input.bind("<Return>", lambda event: self.updateTaskTitle())
        self.okButton = ctk.CTkButton(
            self.boxInput,
            command=self.updateTaskTitle,
            text="Ok",
            width=50,
            cursor="hand2",
        )

        self.boxButton = ctk.CTkFrame(self, height=50)
        self.editButton = ctk.CTkButton(
            self.boxButton,
            text="",
            command=self.toggleBox,
            image=ctk.CTkImage(
                dark_image=Image.open("assets/whiteEdit.png"),
                light_image=Image.open("assets/blackEdit.png"),
                size=(20, 20),
            ),
            width=30,
            height=30,
            fg_color="transparent",
            hover_color=("#9E9E9E", "#424242"),
            cursor="hand2",
        )
        self.deleteButton = ctk.CTkButton(
            self.boxButton,
            text="",
            command=self.deleteTask,
            image=ctk.CTkImage(
                dark_image=Image.open("assets/whiteCross.png"),
                light_image=Image.open("assets/blackCross.png"),
                size=(20, 20),
            ),
            width=30,
            height=30,
            fg_color="transparent",
            hover_color=("#f82e57", "#f82e57"),
            cursor="hand2",
        )

    def show(self) -> None:
        self.pack(pady=5)
        self.checkbox.place(relx=0.02, rely=0.2)
        self.label.place(relx=0.1, rely=0.2)
        self.boxButton.place(relx=0.85, rely=0.2)
        self.editButton.grid(row=0, column=0, padx=2, pady=2)
        self.deleteButton.grid(row=0, column=1, padx=2, pady=2)

    def toggleBox(self) -> None:
        if self.isEditing:
            self.boxInput.place_forget()
            self.input.grid_forget()
            self.okButton.grid_forget()
            self.label.place(relx=0.1, rely=0.2)
        else:
            self.label.place_forget()
            self.boxInput.place(relx=0.1, rely=0.2)
            self.input.grid(row=0, column=0, padx=2, pady=2)
            self.okButton.grid(row=0, column=1, padx=2, pady=2)

        self.isEditing = not self.isEditing

    def updateTaskTitle(self) -> None:
        payload = {
            "title": self.entryValue.get(),
        }
        self.label.configure(text=payload["title"])
        self.handleEditTask(self.task["id"], payload)
        self.toggleBox()

    def updateTaskCompleted(self) -> None:
        payload = {
            "completed": self.checkboxValue.get(),
        }
        self.handleEditTask(self.task["id"], payload)

    def deleteTask(self) -> None:
        name = "!taskitem" if self._id == 0 else f"!taskitem{self._id + 1}"
        self.handleDeleteTask(self.task["id"], name)
