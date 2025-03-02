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


# 05. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.

Celsius = int(input("Enter the temperature in Celsius Degree: "))

Fahrenheit = ((Celsius * 9 / 5) + 32)

print(Fahrenheit)


# 04. Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.

number = [10, 15, 30, 40]

string = [str(num) for num in number]

print(string)


# 16. Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

input_time = int(input("Enter the time in 24-hour format: "))


if 5 <= input_time <12:

    print("Good Morning!")

elif 12 <= input_time <18:

    print("Good Afternoon!")

elif 18 <= input_time <21:

    print("Good Evening!")

else:
    print("Good Night!")



# 15. Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

single_character = input("Enter a single_character here: ").lower()

if (single_character == "a") or (single_character == "e") or (single_character == "i") or (single_character == "o") or (single_character == "u"):
    print(f"{single_character} is vowel")

else:
     print(f"{single_character} is Consonant")



# 19. Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.

take_number = int(input("Enter the number: "))

if 0<= take_number <=50:
    print(f"The number {take_number} falls within the ranges: 0-50")

elif 51<= take_number <=100:
    print(f"The number {take_number} falls within the ranges: 51-100")

elif 101<= take_number <=150:
    print(f"The number {take_number} falls within the ranges: 101-150")

elif 151<= take_number:
    print(f"The number {take_number} above range 150")


# 41. List Element Count: Write a Python program to count the occurrences of a specific element in a given list.

