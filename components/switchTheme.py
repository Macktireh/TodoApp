import customtkinter as ctk


class SwitchTheme(ctk.CTkSwitch):
    def __init__(self, parent: ctk.CTk) -> None:
        self.parent = parent
        self.value = ctk.StringVar(value="dark")
        self.text = ctk.StringVar(value="dark")

        super().__init__(
            self.parent,
            text=self.text.get(),
            variable=self.value,
            command=self.setTheme,
            onvalue="dark",
            offvalue="light",
        )

    def show(self) -> None:
        self.pack(pady=10)

    def setTheme(self) -> None:
        ctk.set_appearance_mode(self.value.get())
        self.configure(text=self.value.get())
