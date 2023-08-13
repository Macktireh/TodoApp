import tkinter as tk
from components.countTasks import CountTask

from services import TodoService


class TodoApp:
    def __init__(self):
      self.root = tk.Tk()
      self.root.title("Todo List")
      self.root.geometry("750x450")
      self.root.config(background="#32405b")
      
      self.taks = []

      self.heading = tk.Label(
        self.root, 
        text="Python dans le navigateur",
        font="arial 20 bold", 
        fg="white", bg="#32405b"
      )
      self.heading.pack(pady=30)

      self.countTask = CountTask(parent=self.root)
      self.countTask.show()

    def start(self):
        self.root.mainloop()


app = TodoApp()
app.start()

