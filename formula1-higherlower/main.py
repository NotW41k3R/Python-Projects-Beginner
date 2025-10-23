import random
import game_data
import art
import os
import time

def compare(a,b):
    if a['follower_count']>b['follower_count']:
        return 'a'
    elif a['follower_count']<b['follower_count']:
        return 'b'
    else: 
        return None
    
def play(choice_a,choice_b):
    start='y'
    high_score=0
    score=0
    while start=='y':
        print(art.logo)
        print(f"Compare A: {choice_a['name']}, {choice_a['description']}, {choice_a['country']}")
        print(art.vs)
        print(f"Against B: {choice_b['name']}, {choice_b['description']}, {choice_b['country']}")
        print('\n')
        result = compare(choice_a,choice_b)
        if result == None:
            while choice_a['follower_count']==choice_b['follower_count']:
                choice_b=random.choice(game_data.data)
            continue

        choice = input("Who has more Followers? A or B: ").lower()

        if choice==result:
            score += 1
            high_score=max(high_score,score)
            print(f"That's Correct! Current score: {score}, High Score: {high_score}")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"That's Correct! Current score: {score}, High Score: {high_score}")
            choice_a = choice_b
            choice_b = random.choice(game_data.data)
            while choice_b == choice_a:
                choice_b = random.choice(game_data.data)

            continue
        else:
            print(f"That's Incorrect :(  Final Score: {score}, High Score: {high_score}")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"That's Incorrect :(  Final Score: {score}, High Score: {high_score}")
            score=0
            start=input("Do you want to try again? y or n: ").lower()
            
            

#Initializing
choice_a, choice_b=random.sample(game_data.data , 2)
play(choice_a,choice_b)