from calculator_app.model.calculator_model import CalculatorModel
from calculator_app.view.calculator_view import CalculatorView
from calculator_app.controller.calculator_controller import CalculatorController

def run_app():
    model = CalculatorModel()
    view = CalculatorView(None)
    controller = CalculatorController(model, view)
    view.controller = controller
    view.bind_events() 
    view.mainloop()

