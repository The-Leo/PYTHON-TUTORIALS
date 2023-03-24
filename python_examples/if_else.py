# Collect string and test it's length
# This is something you will do when validating passwords. 
input = input("Please enter a test string: ")

if len(input) < 6:
    print("Your string is too short.")
    print("Please enter a new string with at least 6 characters.")

