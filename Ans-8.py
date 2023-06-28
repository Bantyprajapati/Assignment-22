# Write a recursive python function to print binary of a given decimal number.
def print_binary(n):
    if n > 1:
        print_binary(n // 2)
    print(n % 2, end='')

# Test the function
number = 10
print("Binary representation of", number, "is:", end=' ')
print_binary(number)
