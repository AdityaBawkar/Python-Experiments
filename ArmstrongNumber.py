# Experiment 8: Armstrong Number Check
# Example: 153 = 1^3 + 5^3 + 3^3

num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
