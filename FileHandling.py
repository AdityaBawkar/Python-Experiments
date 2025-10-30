# Experiment 2: File Handling
# Objective: To demonstrate writing to and reading from a file

# Writing to a file
file_name = "sample.txt"
with open(file_name, "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python file handling is easy!")

print("Data written successfully to", file_name)

# Reading from a file
with open(file_name, "r") as file:
    content = file.read()

print("\nData read from file:")
print(content)
