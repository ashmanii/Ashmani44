# Simple Palindrome Checker

# Ask the user to enter a string or number
user_input = input("Enter a string or number: ")

# Convert the input to string (in case of number)
user_input = str(user_input)

# Reverse the input
reversed_input = user_input[::-1]

# Check if input is same as its reverse
if user_input == reversed_input:
    print(" It is a palindrome.")
else:
    print(" It is not a palindrome.")

input("Press Enter to exit...")
