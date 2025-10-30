# Experiment 4: Fibonacci Series
# Objective: To generate Fibonacci series up to n terms

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

terms = int(input("Enter number of terms: "))

print("Fibonacci Series:", fibonacci(terms))
