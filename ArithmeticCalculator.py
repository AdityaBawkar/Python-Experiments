# Experiment 1: Simple Arithmetic Calculator
# Objective: To perform basic arithmetic operations (add, subtract, multiply, divide)

def add(a, b):
    return a + b  # returns sum

def subtract(a, b):
    return a - b  # returns difference

def multiply(a, b):
    return a * b  # returns product

def divide(a, b):
    if b != 0:
        return a / b  # returns quotient
    else:
        return "Error: Division by zero!"

# User input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
