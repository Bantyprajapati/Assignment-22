# Write a recursive python function to find the Nth term of the Fibonacci series.
def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
N = 10
nth_term = fibonacci(N)
print("The", N, "th term of the Fibonacci series is:", nth_term)
