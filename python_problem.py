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



# 12. Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third Number: "))

if a>b:
    print(f"The Largest Number is {a}")

elif b>c:
    print(f"The Largest Number is {b}")

else:
    print(f"The Largest Number is {c}")


# 45. Flatten Nested List: Write a Python program to flatten a given nested list and convert it into a single-dimensional list.

list = [["Rifat", "Shajid", "Tutul"], [20, 30, 32]]

single_list = (list[0] + list[1])

print(single_list)


# 13. Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not.

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 ==0 and year % 100 !=0):
    print(f"{year} is Leap year")
else:
    print(f"{year} is Not-Leap year")



# 37. List Sorting: Write a Python program to sort a list of integers in ascending order.
number = [10, 15, 9, 8, 0, 5, 80, 60, 45, 100]
number.sort()

print(number)
