from asteval import Interpreter
import math

class CalculatorModel:
    def __init__(self):
        self.expression = ""
        self.history = []
        self.asteval = Interpreter()
        self.asteval.symtable.clear()
        self.asteval.symtable.update({
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'sqrt': math.sqrt,
            'pi': math.pi,
            'e': math.e,
            'abs': abs,
            'round': round,
            'pow': pow
        })

    def add_input(self, char):
        self.expression += char

    def backspace(self):
        self.expression = self.expression[:-1]

    def clear(self):
        self.expression = ""

    def evaluate(self):
        try:
            result = self.asteval(self.expression)
            if self.asteval.error:
                raise Exception("Eval error")
            result = str(result)
            self.history.append(f"{self.expression} = {result}")
            self.expression = result
            return result
        except ZeroDivisionError:
            self.expression = ""
            return "Eroare: /0"
        except Exception:
            self.expression = ""
            return "Eroare"

    def get_expression(self):
        return self.expression

    def get_history(self, limit=5):
        return self.history[-limit:]
