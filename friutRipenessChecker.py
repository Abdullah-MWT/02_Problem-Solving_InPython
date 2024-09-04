# ++++++++++++++ Friut Ripeness Checker ++++++++++++++


fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
fruitColors = ['Green', 'Yellow', 'Brown']

print('Fruits: ')
for x in fruits:
    print(x)

print('\n')

print('Colors: ')
for x in fruitColors:
    print(x)

enetrFruit = input("Please Enter Your Fruit Name: ")
enterFruitColor = input("Please Enter Your Fruit Color: ")

if enetrFruit in fruits and enterFruitColor == 'Green':
    print("Your Fruit is Unripe")
elif enetrFruit in fruits and enterFruitColor == 'Yellow':
    print("Your Fruit is Ripe")
elif enetrFruit in fruits and enterFruitColor == 'Brown':
    print("You Fruit is OverRiped")
else:
    print("You may Have Enterd the wrong Fruit Name or Color")
