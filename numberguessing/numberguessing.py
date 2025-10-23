import random
import logo


start='y'
while start=='y':
    print(logo.logo)
    number = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty, type easy or hard: ").lower()
    attempts=10
    if difficulty=='hard':
        attempts=5
    print(f"Guess the number in {attempts} attempts")
    for i in range(1,attempts+1):
        remaining_attempts = attempts - i
        guess=int(input("Guess the Number: "))

        if guess==number:
            print("That's Right!")
            start = input("Do you want to play again? y or n: ").lower()
            break
        elif guess>number:
            print("Too High")
        else:
            print("Too Low")
        
        if remaining_attempts>0:
            print(f"You have {remaining_attempts} attempts left")
        else:
            print("You've run out of attempts")
            print(f"Correct answer was {number}")
            start = input("Do you want to play again? y or n: ").lower()