class CalculatorLogic:
    def __init__(self):
        pass
    
 #Addition Function (Bermudo)
    def add(self, x, y):
        return x + y
    
 # Subtraction Function (Espina)
    def sub(self, x, y):
        return x - y

 # Division Function (Palongpalong)
    def divide(self, x, y):
        if y == 0:
            return "Error: Div by 0"
        return x / y
    
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
