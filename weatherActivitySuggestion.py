# +++++++++++++ Weather Activity Suggestion ++++++++++++++

weather = (input("Please Enter Today's Weather: ")).lower()

if weather == 'sunny':
    print("Please! Go For a Walk")
elif weather == 'rainy':
    print("Please! Read a Book")
elif weather == 'snowy':
    print('Please! Go Outside and Buid a Snowman')
else:
    print("Something Went Wrong")