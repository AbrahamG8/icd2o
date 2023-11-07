# Check if a number is positive.
number = int(input("Please entera a number: "))
if number > 0:
    print(f"{number} is positive")

if number <= 0:
    print(f"{number} is not positive")

# Determine if a person can vote (age 18 or older).
age = int(input("Please enter your age: "))


if age >= 18:
    not_eligible = ""

if age < 18:
    eligible = "not"

print(f"You are eligible to {eligible} to vote.")

print(f"You are eligible to vote.")

if age >= 18:
    print(f"You are eligible to vote")

if age < 18:
    print(f"You are not eligible to vote")



# Check if a string is empty.
str = input("Please enter a string")
if len(str) ==0:
    print("The string is empty")

if len(str) != 0:
    print("The string is not Empty")


# Write a function that determines the maximum of two numbers.
def max_number(a,b):
    if a > b:
        return a

    return b
print(max_number(4,5))
print(max_number(14,5))

# Check if a user's input is equal to a secret password.
def password_checker (password, user_input):
    if password == user_input:
        return True
    
    return False


# Write a function that checks if a number is within a specific range (1-10 inclusive).

def range_checker (num, lower, upper):
    if lower <= number <= upper:
        return True
    
    return False

a = int(input("Please enter a number between 1-10:"))
if range_checker(a, 1, 10):
    print("Good you listen to the Instructions!")

if range_checker(a, 1, 10):
    print("ARGHHHH!! i am not happy becaus eyou DON'T Listen")


# Write a function that accepts a numberical grade and returns the Letter Grade

def grade_converter (grade):
    if grade >= 80:
        return "A"
    if grade >= 70:
        return "B"
    if grade >= 60:
     return "C"
    if grade >= 50:
        return "D"
     
