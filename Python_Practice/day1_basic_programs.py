# Python Day 1 Basic Programs

# 1. Introduction program
print("Program 1: Introduction")

name = "Ananya"
course = "Python"
goal = "AIML and placements"

print("My name is", name)
print("I am learning", course)
print("My goal is to become strong in", goal)


# 2. Simple calculator
print("\nProgram 2: Simple Calculator")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)


# 3. Even or Odd
print("\nProgram 3: Even or Odd")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 4. Marks Grade Program
print("\nProgram 4: Marks Grade")

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")


# 5. Multiplication Table
print("\nProgram 5: Multiplication Table")

num = int(input("Enter number for table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
