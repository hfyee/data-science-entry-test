def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if isinstance(num, int) and isinstance(divisor, int):
        try:
            if num % divisor == 0:
                return True
            else:
                return False
        except ZeroDivisionError:
            print("Cannot divide a number by zero.")
            return False

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))
print(check_divisibility(15, 0))
