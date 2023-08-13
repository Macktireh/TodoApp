import customtkinter as ctk

from components.countTasks import TaskCounter


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Todo List")
        self.geometry("750x450")
        self.config(background="#32405b")

        self.taks = []

        self.heading = ctk.CTkLabel(
            self,
            text="Application Todo List",
            font=("arial", 30, "bold"),
            text_color=("#FFF", "#FFF"),
            fg_color="#32405b",
        )
        self.heading.pack(pady=20)

        self.countTask = TaskCounter(parent=self)
        self.countTask.show()

    def start(self) -> None:
        self.mainloop()


if __name__ == "__main__":
    App().start()
