n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
print("hi")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
print(f"The factorial of {number} is {factorial(number)}")
