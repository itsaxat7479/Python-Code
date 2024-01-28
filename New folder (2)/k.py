class NegativeValueError(Exception):
    """Custom exception class for negative values."""

    def __init__(self, value):
        self.value = value
        super().__init__(f"NegativeValueError: Negative value not allowed - {value}")


def divide_numbers(a, b):
    # Check if either parameter is negative
    if a < 0 or b < 0:
        raise NegativeValueError("One or both parameters are negative")

    try:
        result = a / b
        return result

    except ZeroDivisionError:
        print("Error: Division by Zero")
        return None

    except (TypeError, ValueError):
        print("Error: Invalid input types")
        return None

# Test cases
# Case 1: Successful division
result1 = divide_numbers(10, 2)
print(f"Result 1: {result1}")

# Case 2: Division by zero
result2 = divide_numbers(5, 0)

# Case 3: Invalid input types (e.g., string instead of number)
result3 = divide_numbers("abc", 2)

# Case 4: Valid input types but ValueError (e.g., float instead of int)
result4 = divide_numbers(10.5, 2)

# Case 5: Negative value (should raise NegativeValueError)
try:
    result5 = divide_numbers(-15, 3)
except NegativeValueError as e:
    print(e)
    result5 = None

# Case 6: Valid input types and successful division
result6 = divide_numbers(15, 3)
print(f"Result 6: {result6}")
