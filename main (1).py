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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

Direction = input('You\'re a crossroad. Where do you want to go? Type "left" or "right"').lower()

#Direction = Direction.lower()

if Direction == "left":
  river = input("You come to lake. There is an island in the middle of the lake. Type 'Wait' to wait for a boat. Type 'swim' to swim across. ")
  
  river = river.lower()
  
  if river == 'wait':

    
    Door = input("You Arraived the island unharmed. there is a house of there doors. One Red, one Yellow and one Blue. which color do you chooes? ")
    Door = Door.lower();
    if Door == "red":
      print("Burned by Fire. Game Over.")
    elif Door == "blue":
      print("Eaten by beasts. Game Over")
    elif Door == "yellow":
      print("You Win!")
    else:
      print("Game Over")

  
  elif river == "swim":
    print("Attacked by trout. Game Over.")
  else:
    print("Game Over")


elif Direction == "right":
  print("Fall into a hole. Game Over.")


else:
  print("Game Over")