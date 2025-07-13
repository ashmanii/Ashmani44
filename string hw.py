# 1. Indexing and Slicing
# Given the string s = "PythonPractice", what are the outputs of:
# - s[1]
# - s[-3:]
# - s[2:7]
# s = "Pythonpractice"
# print(s[1])
# print(s[-3:])
# print(s[2:7])


# 2. Reverse a String
# Write a one-liner to reverse the string "developer" using slicing.
# print("developer"[::-1])

# Count Vowels
# Write a function that counts the number of vowels in a given string


# def vowel_letters(st):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in st:
#         if char in vowels:
#             count += 1
#         return count


# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count


# st = "Hello, World"
# print(count_vowels(st))

# 4. Check for Palindrome
# Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.
# def is_palindrome(text):
#     # Remove spaces and convert to lowercase
#     cleaned = text.replace(" ", "").lower()

#     # Check if the cleaned string is equal to its reverse
#     return cleaned == cleaned[::-1]


# Example usage
# print(is_palindrome("Race car"))      # True
# print(is_palindrome("Hello"))         # False
# print(is_palindrome("Was it a car or a cat I saw"))  # True

# 5. Clean and Format String
# Given text = "   hello world! welcome to Python.   ", write code to:
# - Remove leading/trailing spaces
# - Capitalize each word
# - Replace the word "Python" with "Programming"
# text = "   hello world! welcome to Python.   "

# # Step 1: Remove leading/trailing spaces
# text = text.strip()

# # Step 2: Capitalize each word
# text = text.title()

# # Step 3: Replace "Python" with "Programming"
# text = text.replace("Python", "Programming")

# print(text)

# 6. Find Longest Word
# Write a function that takes a sentence and returns the longest word in it.


# def find_longest_word(sentence):
#     # Remove punctuation (optional)
#     words = sentence.split()

#     # Find the longest word using max() and len() as the key
#     longest = max(words, key=len)

#     return longest


# # Example usage
# print(find_longest_word("Python is a powerful programming language"))

# 7. String Operators
# Given s1 = "Py" and s2 = "thon", what are the results of:
# - s1 + s2
# - s1 * 3
# - "y" in s1
# s1 = "Py"
# s2 = "thon"

# # 1. Concatenation
# result1 = s1 + s2
# print("s1 + s2 =", result1)

# # 2. Repetition
# result2 = s1 * 3
# print("s1 * 3 =", result2)

# # 3. Membership test
# result3 = "y" in s1
# print('"y" in s1 =', result3)

# 8. Remove Duplicate Characters
# Write a function that removes all duplicate characters from a string but keeps the first occurrence.


# def remove_duplicates(text):
#     result = ""
#     for char in text:
#         if char not in result:
#             result += char
#     return result


# # Example usage
# print(remove_duplicates("programming"))

# 9. Check for Anagram
# Write a function that returns True if two strings are anagrams of each other.
# def are_anagrams(str1, str2):
#     # Remove spaces and convert to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     # Compare sorted characters
#     return sorted(str1) == sorted(str2)


# # Example usage
# print(are_anagrams("listen", "silent"))          # True
# print(are_anagrams("Hello", "Olelh"))            # True
# print(are_anagrams("Python", "Java"))            # False

# 10. Word Frequency Counter
# Write a function that takes a sentence and returns a dictionary of word frequencies.


# def word_frequency(sentence):
#     # Convert to lowercase and split into words
#     words = sentence.lower().split()

#     # Create a dictionary to store word counts
#     freq = {}
#     for word in words:
#         if word in freq:
#             freq[word] += 1
#         else:
#             freq[word] = 1
#     return freq


# # Example usage
# text = "Python is great and Python is fun"
# print(word_frequency(text))
