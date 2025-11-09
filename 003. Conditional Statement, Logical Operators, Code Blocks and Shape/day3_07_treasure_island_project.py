print('''

******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')

print("Welcome to Treasure Island.")
print("You're mission is to find the treasure.")
choice = input("You're at a cross road. Where do you want to go? (Type 'left' or 'right'): ")

if choice.lower() == "left":
    print("You've come at lake. There is an island in the middle of the lake.")
    choice = input("(Type 'wait' to wait for a boat. Type 'swim' to swim accros): ")
    if choice.lower() == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        choice = input("One red, one yellow and one blue. Which colour do you choose?: ")
        if choice.lower() == "red":
            print("It's a room full of fire. Game Over!")
        elif choice.lower() == "blue":
            print("You enter a room of beasts. Game Over!")
        elif choice.lower() == "yellow":
            print("Congratulations! You found the treasure!")
    else:
        print("You get attacked by an angry trout. Game Over!")
    
else:
    print("You fell into a hole. Game Over!")
