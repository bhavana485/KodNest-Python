def add():
    return a + b

def subtract():
    return a - b 

def multiply():
    return a * b

def divide():
    return a / b

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print(f"Addition of the two numbers: {add(num1, num2)}")
print(f"Subtraction of the two numbers: {subtract(num1, num2)}")
print(f"Multiplication of the two numbers: {multiply(num1, num2)}")
print(f"Division of the two numbers: {divide(num1, num2)}")
