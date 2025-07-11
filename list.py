L1 = [1, 8, 7, 2, 21, 15]

# L1.sort()
# print(L1)

# L1.append(8)
# print(L1)

# L1.insert(3, 8)
# print(L1)

# L1.reverse()
# print(L1)

# L1.append(8)
# last_item = L1.pop()
# print(last_item)
# print(L1)

# third_item = L1.pop(2)
# print(third_item)
# print(L1)

# L1.remove(7)
# print(L1)


# WAP to store 7 fruits in a list entered by the user.
fruits = []

# for i in range(7):
#     fruit = input(f"Enter fruit {i+1}: ")
#     fruits.append(fruit)
# print("The list of fruits is:", fruits)


# # WAP to accept marks of 6 students and display them in a sorted manner.
marks = []

for i in range(6):
    mark = int(input(f"Enter marks for student {i+1}: "))
    marks.append(mark)

marks.sort()
print("Sorted marks are:", marks)
