class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def on_button_pressed(self, char):
        if char == 'C':
            self.model.clear()
        elif char == '⌫':
            self.model.backspace()
        elif char == '=' or char == 'Enter':
            self.model.evaluate()
        else:
            self.model.add_input(char)
        self.update_view()

    def on_key_press(self, event):
        if event.char in "0123456789+-*/().":
            self.model.add_input(event.char)
            self.update_view()

    def update_view(self):
        self.view.update_display(self.model.get_expression())
        self.view.update_history(self.model.get_history())
