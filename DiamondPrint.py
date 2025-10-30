# Experiment 9: Diamond Pattern
# Prints a diamond star pattern

rows = int(input("Enter number of rows: "))

# Upper part
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Lower part
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
