import random

possibilities = ['''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''' , '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''' , '''
SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''' ]

computer_choice = random.randint(0,2)
user_choice_str = input("Choose Rock(0), Paper(1) or Scissor(2)\n")
user_choice = int(user_choice_str)

result = (user_choice - computer_choice) % 3
if result==0:
    print(f"Computer chose")
    print(possibilities[computer_choice])
    print(f"You chose")
    print(possibilities[user_choice])
    print("It is a Draw")
elif result==1:
    print(f"Computer chose")
    print(possibilities[computer_choice])
    print(f"You chose")
    print(possibilities[user_choice])
    print("You Win!")
else:
    print(f"Computer chose")
    print(possibilities[computer_choice])
    print(f"You chose")
    print(possibilities[user_choice])
    print("You Lose")