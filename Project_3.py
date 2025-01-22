print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************
''')
print()
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")

fd1 = input('You are at a crossroad now! Which direction you are going to take! ("Left" or "Right") : ').lower()

if fd1 == "right" or fd1 == "r":
    print("Damn, You met up with Gorlock the Destroyer! You were Consumed!")
    print("Game Over!!!")
elif fd1 == "left" or fd1 == "l":
    print("Excellent Choice! Now you have reached a lake!")
    fd2 = input('Enter which option you are going to take! ("Wait" for a boat or "Swim")!')
    if fd2 == "swim" or fd2 == "s":
        print("You have been devoured by the whale, who is the friend of the 10/10!")
        print("Game Over!!!")
    elif fd2 == "wait" or fd2 == "w":
        print("Good Patience Fellow Adventurer! You just been picked up by the Titanic!")
        print("Now you have reached the island, and you seem to notice three \"Anywhere Door\" from \"Doraemon\". You see a red door and a green door!")
        fd3 = input("Enter the door you are picking! ('Red' or 'Green' or 'Yellow')!").lower()
        if fd3 == "red" or fd3 == "r":
            print("You entered the room full of fire and gaseous release of Mr. Perfect AA! Game Over!")
        elif fd3 == "green" or fd3 == "g":
            print("You have entered the room of beasts, which are the children of gorlock! Game Over!")
        elif fd3 == "yellow" or fd3 == "y":
            print("You have found the treasure! You have Won !!!!!!!!!!!!!!!!")
        else:
            print("Invalid Entry!")

    else:
        print("Invalid Entry!")

else:
    print("Invalid Entry!")
