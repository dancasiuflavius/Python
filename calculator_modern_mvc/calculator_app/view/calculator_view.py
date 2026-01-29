import customtkinter as ctk

class CalculatorView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("Calculator Modern")
        self.geometry("320x500")
        ctk.set_appearance_mode("dark")

        self.create_widgets()

    def create_widgets(self):
        self.entry = ctk.CTkTextbox(self, height=60, font=("Consolas", 20), wrap="none")
        self.entry.pack(padx=10, pady=(20, 10), fill="x")
        self.entry.insert("end", "")
        self.entry.configure(state="disabled")

        self.history_label = ctk.CTkLabel(self, text="Istoric:", font=("Arial", 14))
        self.history_label.pack(padx=10, anchor="w")

        self.history_box = ctk.CTkTextbox(self, height=100, font=("Consolas", 12), wrap="none")
        self.history_box.pack(padx=10, pady=(0, 10), fill="both")
        self.history_box.configure(state="disabled")

        buttons = [
            ['7', '8', '9', '/', '('],
            ['4', '5', '6', '*', ')'],
            ['1', '2', '3', '-', '⌫'],
            ['0', 'C', '=', '+', 'Enter']
        ]

        for row in buttons:
            frame = ctk.CTkFrame(self)
            frame.pack(pady=3, padx=10, fill="x")
            for char in row:
                btn = ctk.CTkButton(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    width=50,
                    height=40,
                    command=lambda c=char: self.controller.on_button_pressed(c)
                )
                btn.pack(side="left", expand=True, padx=3)

    def bind_events(self):
        self.bind("<Key>", self.controller.on_key_press)
        self.bind("<BackSpace>", lambda e: self.controller.on_button_pressed("⌫"))
        self.bind("<Return>", lambda e: self.controller.on_button_pressed("="))
        self.bind("<KP_Enter>", lambda e: self.controller.on_button_pressed("="))

    def update_display(self, text):
        self.entry.configure(state="normal")
        self.entry.delete("1.0", "end")
        self.entry.insert("end", text)
        self.entry.configure(state="disabled")

    def update_history(self, lines):
        self.history_box.configure(state="normal")
        self.history_box.delete("1.0", "end")
        for line in lines:
            self.history_box.insert("end", line + "\n")
        self.history_box.configure(state="disabled")
