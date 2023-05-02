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

#Write your code below this line 👇
import random
playerChoice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors."))
choices = [rock, paper, scissors]
compChoice = random.randint(0,2)
print(f"You chose:\n{choices[playerChoice]})")
print(f"Computer chose:\n{choices[compChoice]}")
if ((playerChoice == 0) and (compChoice == 2)):
    state = "win"
elif ((playerChoice == 2) and (compChoice == 1)):
    state = "win"
elif ((playerChoice == 1) and (compChoice == 0)):
    state = "win"
elif playerChoice == compChoice:
    state = "tie"
else:
    state = "lose"
print(f"You {state}")

