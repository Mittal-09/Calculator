class BasicCalculator:
    """
    Simple calculator supporting add, subtract, multiply, divide, power, modulus.
    Methods raise ValueError for invalid input types and ZeroDivisionError for division by zero.
    """
    def _check_numbers(self, *args):
        for a in args:
            if not isinstance(a, (int, float)):
                raise ValueError("Operands must be int or float, got: {}".format(type(a)))
    def add(self, a, b):
        self._check_numbers(a, b)
        return a + b
    def subtract(self, a, b):
        self._check_numbers(a, b)
        return a - b
    def multiply(self, a, b):
        self._check_numbers(a, b)
        return a * b
    def divide(self, a, b):
        self._check_numbers(a, b)
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    def power(self, a, b):
        self._check_numbers(a, b)
        return a ** b
    def modulus(self, a, b):
        self._check_numbers(a, b)
        if b == 0:
            raise ZeroDivisionError("Modulus by zero")
        return a % b
        print(bakchod)
print(sum([1,2,3]))