# Write a recursive python function to calculate sum of first N even natural numbers
def calculate_sum_even_numbers(n):
    if n == 1:
        return 2
    else:
        return 2 * n + calculate_sum_even_numbers(n - 1)

# Test the function
N = 5
sum_of_even_numbers = calculate_sum_even_numbers(N)
print("Sum of the first", N, "even natural numbers:", sum_of_even_numbers)
