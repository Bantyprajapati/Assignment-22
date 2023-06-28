# Write a recursive python function to calculate sum of cubes of first N natural numbers
def calculate_sum_of_cubes(n):
    if n == 1:
        return 1
    else:
        return n ** 3 + calculate_sum_of_cubes(n - 1)

# Test the function
N = 5
sum_of_cubes = calculate_sum_of_cubes(N)
print("Sum of cubes of the first", N, "natural numbers:", sum_of_cubes)
