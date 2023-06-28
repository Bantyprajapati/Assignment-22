# Write a recursive python function to calculate sum of squares of first N natural numbers
def calculate_sum_of_squares(n):
    if n == 1:
        return 1
    else:
        return n ** 2 + calculate_sum_of_squares(n - 1)

# Test the function
N = 5
sum_of_squares = calculate_sum_of_squares(N)
print("Sum of squares of the first", N, "natural numbers:", sum_of_squares)
