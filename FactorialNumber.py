# Experiment 6: Factorial of a Number
# Uses recursion to calculate factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
