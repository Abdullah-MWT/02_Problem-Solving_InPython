# ++++++++++++ Movie Ticket Pricing ++++++++++++++

userAge = int(input("Please Enter Your Age: \n"))
adultsPrice = " $18"

if userAge < 18:
    print('You Should Pay $12')
elif userAge > 18:
    print("You Should pay $18")
else:
    print("You Should Pay $15")

discount = input("Do you want Discount? \n")
day = input("Please Enter the Day You Will watch Movie On: \n")
if day == "Saturday" or day == "Sunday":
    if discount == "Yes":
        print("You Should Pay $10")
    else:
        print("You Should Pay $15")
else:
    print("You Should Pay $18")






