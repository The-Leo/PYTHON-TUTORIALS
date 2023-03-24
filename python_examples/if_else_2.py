# Prompt a use to enter a number and test if it is even or odd
input = input("Please enter an integer: ")
number = int(input)

if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")