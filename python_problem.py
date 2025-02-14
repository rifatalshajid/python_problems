# 01. Variable Swap: Write a Python program to swap the values of two variables without using a temporary variable.

a = 10
b = 20

a,b = b,a

print(a , b)


# 02. Even or Odd: Write a Python program that takes an integer as input and prints whether it is even or odd.

number = int(input("Enter the number" ))

if (number % 2) == 0:
    print(f"{number} is a Even Number")
else:
    print(f"{number} is Odd number")


# 06. Data Type Checker: Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).

def dataTypeCheck(variable):
    return type(variable).__name__

print(dataTypeCheck(10))
print(dataTypeCheck(10.0))
print(dataTypeCheck("Rifat"))
print(dataTypeCheck(["Rifat", "Shajid"]))
