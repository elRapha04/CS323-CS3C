class CalculatorLogic:
    def __init__(self):
        pass

    def evaluate(self, expression):
        """
        Evaluates a mathematical expression string.
        Returns the result as a string or 'Error' if invalid.
        """
        try:
            result = eval(expression)
            return str(result)
        except ZeroDivisionError:
            return "Error: Div by 0"
        except Exception:
            return "Error"
