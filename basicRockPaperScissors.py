import random


rock = """
              _
             / )
            / /    _
  _        / /    / )
 ( `.     / /-.  / /
  `\\ \\   / // /`/ /
    ; `-`  (_/ / /
    |       (_/ /
    \\          /
     )       /`
    /      /`
"""

scissors = """
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \\  `(.-')
   > ._>-'
  / \\/
"""

paper = """
     _.-._
    | | | |_
    | | | | |
    | | | | |
  _ |  '-._ |
  \\`\\`-.'-._;
   \\    '   |
    \\  .`  /
     |    |

"""

usr_choice = int(input("What do you choose? \nType 0 for rock, 1 for paper & 2 for scissor\n-->"))
if(usr_choice >= 3 or usr_choice < 0):
    print("You Chose an Invalid number. Choose another number.")
else:
    if(usr_choice == 0):
        print(rock)
    elif(usr_choice == 1):
        print(paper)
    elif(usr_choice == 2):
        print(scissors)
        

    comp_choice = random.randint(0, 2);
    print("Computer Chose: ")
    if(comp_choice == 0):
        print(rock)
    elif(comp_choice == 1):
        print(paper)
    elif(comp_choice == 2):
        print(scissors)

    if(usr_choice == comp_choice):
        print("It's a tie.")
    elif(usr_choice == 0 and comp_choice == 1):
        print("You Lose")
    elif(usr_choice == 0 and comp_choice == 2):
        print("You Win")
    elif(usr_choice == 1 and comp_choice == 0):
        print("You Win")
    elif(usr_choice == 1 and comp_choice == 2):
        print("You Lose")
    elif(usr_choice == 2 and comp_choice == 0):
        print("You Lose")
    elif(usr_choice == 2 and comp_choice == 1):
        print("You Win")