class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def calculate(self, operation: str):
        operation = operation.lower()
        if operation == "addition":
            return self.a + self.b
        elif operation == "subtraction":
            return self.a - self.b
        elif operation == "multiplication":
            return self.a * self.b
        elif operation == "division":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"
