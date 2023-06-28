# Write a recursive python function to calculate the factorial of a number.
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Test the function
number = 5
factorial = calculate_factorial(number)
print("Factorial of", number, "is:", factorial)
