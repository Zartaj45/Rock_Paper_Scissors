import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of choices
choices = [rock, scissors, paper]

# User Input
try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Scissors, or 2 for Paper: "))
    if user_choice < 0 or user_choice > 2:
        raise ValueError("Invalid choice")
except ValueError:
    print("You have entered an invalid number! Please type a number from 0-2!")
else:
    print(f"You chose:\n{choices[user_choice]}")

    # Computer Choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{choices[computer_choice]}")

    # Determining the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 0):
        print("You win!")
    else:
        print("You lose!")
