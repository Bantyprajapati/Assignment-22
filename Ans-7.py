# Write a recursive python function to calculate sum of the digits of a given number
def calculate_sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + calculate_sum_of_digits(n // 10)

# Test the function
number = 12345
sum_of_digits = calculate_sum_of_digits(number)
print("Sum of digits of", number, "is:", sum_of_digits)
