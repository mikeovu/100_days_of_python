import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Creates a list of rock paper scissor images

weapons = [rock, paper, scissors]

# Converts user input to an integer
choice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors. "))

# If the choice is 0 - 2, print the image that maps to the chosen integer. 
# For example, 0 will map to Rock and 2 will map to Scissors.
if choice >= 0 and choice <= 2: 
    print(weapons[choice])

# Have the computer choose a random choice, using the random integer function
# The random.randint function will choose a value between 0 and 2. 
computer_choice = random.randint(0,2)

print("Computer Chose:")

# The weapons image will be chosen based on the integer assigned to the computer_choice variable.

print(weapons[computer_choice])

# If the integer chosen is greater than or equal to 3 and less than 0, you have chosen an invalid number.
if choice >= 3 and choice < 0:
    print("You typed and invalid number. You lose!")
# If your choice is 0, assigned to rock and the computer chooses 2, assigned to scissors, you win.
elif choice == 0 and computer_choice == 2: 
    print("You win!")
# If computer chooses rock and you choose scissors, you lose
elif computer_choice == 0 and choice == 2:
    print("You lose!")
# The choices are now 1(paper) or 2(scissors). Whoever chooses 2 will win.
elif computer_choice > choice: 
    print("You lose!")
elif choice > computer_choice:
    print("You win!")
# If the choice is the same, it's a draw.
elif computer_choice == choice:
    print("It's a draw!")
          












