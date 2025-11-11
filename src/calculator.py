#src/calculator
class Calculator:   
    """Simple calculator with basic operations."""
    def add(self, a, b):
        # TODO: return the sum of a and b
        c= a+b
        return c

    def subtract(self, a, b):
        # TODO: return the difference of a and b
        c= a-b
        
        return c

    def multiply(self, a, b):
        # TODO: return the product of a and b
        c= a-b
        return c

    def divide(self, a, b):
        # TODO: handle division and raise an error if b == 0
        if (b==0):
            raise ZeroDivisionError ("Cannot divide by zero.")
        else:
          c=  a/b
        return c
