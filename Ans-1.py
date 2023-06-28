# Write a recursive python function to calculate sum of first N natural numbers
def calculate_sum_natural_numbers(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum_natural_numbers(n - 1)

# Test the function
N = 5
sum_of_natural_numbers = calculate_sum_natural_numbers(N)
print("Sum of the first", N, "natural numbers:", sum_of_natural_numbers)
