# Write a recursive python function to calculate sum of first N odd natural numbers
def calculate_sum_odd_numbers(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + calculate_sum_odd_numbers(n - 1)

# Test the function
N = 5
sum_of_odd_numbers = calculate_sum_odd_numbers(N)
print("Sum of the first", N, "odd natural numbers:", sum_of_odd_numbers)
