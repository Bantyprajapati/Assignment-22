# Write a recursive python function to print octal of a given decimal number
def print_octal(n):
    if n > 0:
        print_octal(n // 8)
    print(n % 8, end='')

# Test the function
number = 25
print("Octal representation of", number, "is:", end=' ')
print_octal(number)
