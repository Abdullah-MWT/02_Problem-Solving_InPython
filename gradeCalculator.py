# ++++++++++++ Grade Calculator ++++++++++++++

print("Hi, Students! You Are Welcomed")
marks = int(input("Please Enter Your Marks Out Of 100: "))

if marks >= 101:
    print("Don,t You Understand the above line, that Enter marks out of 100 , hahahahahha")
    exit()

if marks >= 90 and marks <= 100:
    print("Hurrah! You Got A Grade Marks")
elif marks >= 80 and marks <= 89:
    print("You Got B Grade Marks") 
elif marks >= 70 and marks <= 79:
    print("You Got C Grade Marks")
elif marks >= 60 and marks <= 69:
    print("You Got D Grade Marks")
else:
    print("You Have Failed the Exam, Try Next Time")

