# ++++++++++++ Movie Ticket Pricing ++++++++++++++

userAge = int(input("Please Enter Your Age: \n"))
day = input("Please Enter the Day You Will watch Movie On: \n")
adultsPrice = " $18"

if userAge < 18:
    print('You Should Pay $12')
elif userAge > 18 & userAge < 30:
    print("You Should pay" + adultsPrice)
else:
    print("You Should Pay $15")

if day == "saturday" or day == "sunday":
    print("You Should Pay $5")



