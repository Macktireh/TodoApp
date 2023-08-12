import tkinter as tk

from services import TodoService


class CountTask:
    def __init__(self, parent):
        self.parent = parent
        self._todeService = TodoService()
        self.textLabel = tk.StringVar(value=f"Tâches à faire : {len(self._todeService.getTasks())}")
    
    def show(self):
        self.label = tk.Label(
          self.parent, 
          textvariable=self.textLabel,
          font="arial 20 bold", 
          fg="white", bg="#32405b"
        ).pack(pady=15)
    
    def setCount(self):
        pass


