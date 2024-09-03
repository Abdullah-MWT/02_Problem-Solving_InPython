# +++++++++++++++ Age Group Categrization ++++++++++++++

age = int(input("Please Enter Your Age: "))

if age < 10:
    print("You are a Kid")
elif age < 18:
    print("You are a Teen")
elif age < 30:
    print("You are Young")
elif age < 60:
    print("You are Middle Aged")
else:
    print("You are Elderly")
