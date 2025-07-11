age = int(input("Enter your age:"))

if age == 18:
    print("You're allowed to drive")
elif age <= 30:
    print("Please use the driving safety guide")
elif age >= 30:
    print("You're older than 30")
else:
    print("You aren't allowed to drive")
