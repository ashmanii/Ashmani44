# 1. Take a number from the user and print whether it's even or odd.

num = int(input("Enter a number to check even or odd: "))
if num % 2 == 0:
    print("thenumber you have enterd is even")
else:
    print("the number you have entered is odd")


# 2. Write a program to count the number of vowels in a given string.
string = input("enter a word to count vowel:  ")
vowel = "AEIOUaeiou"
count = 0

for char in string:
    if char in vowel:
        count += 1

print(count)


# 3. Ask the user to input a sentence and print the number of words in it.

sentence = input("enter a sentence to count the word: ")

words = sentence.split()
print(len(words))


# 4. Take a number from the user and print its multiplication table from 1 to 10 using a function.

def table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")


number = int(input("enter a number for multiplication:  "))

table(number)


# 5. Write a program to accept 5 numbers from the user, store them in a list, and print the maximum and minimum values.

num = []
for i in range(5):
    number = float(input(f"Enter number {i+1}: "))
    num.append(number)

print("the maximum value is: ", max(num))
print("the minimum value is:", min(num))

# 6. Accept a string and check whether it is a palindrome or not (same forward and backward).

text = input("Enter a string to check palindrome: ")

string = text.replace(" ", "").lower()
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# 7. Create a loop that keeps asking the user to guess a secret number between 1 to 10 until they guess it correctly. (Use while loop and break )

secret_num = 5

while True:
    guess = int(input("guess the secret number from 1 to 10 :"))

    if guess == secret_num:
        print("Wow ! You are correct.")
        break

    else:
        print("Better luck next time")


# 8. Accept 5 numbers from the user and store only the even numbers in a new list. Print the final list.

even_number = []
for i in range(5):
    num = int(input(f"Enter a number {i+1}: "))
    if num % 2 == 0:
        even_number.append(num)


print("the even number : ", even_number)


# 9. Write a program that prints the Fibonacci sequence up to n terms. (Ask user for n)


n = int(input("enter a num to check the fibonacci: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("please enter a positive number.")

else:
    print("fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1


# 10. Accept a list of numbers and remove all duplicate values

number = input("Enter numbers separated by spaces: ").split()
number = [int(num) for num in number]

num = list(set(number))
print("without duplicate", num)
