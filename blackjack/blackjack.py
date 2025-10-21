import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(reciever):
    return reciever.append(random.choice(cards))

def calculate_score(deck):
    return sum(deck)

def print_card():
    print(f"Your final cards: {user_cards}, Final score: {user_score}")
    print(f"Dealer's final cards: {computer_cards}, Final score: {computer_score}")

def stand(user_diff, computer_diff):
    if user_diff<computer_diff and user_diff>0:
        print_card()
        print("Congratulation! You Win")
    
    elif user_diff>computer_diff and computer_diff>0:
        print_card()
        print("Better luck next time")

def check_bust(deck):
    score=calculate_score(deck)
    if score>21:
        while 11 in deck and sum(deck) > 21:
            loc=deck.index(11)
            deck[loc]=1
    score=calculate_score(deck)
    if score>21:
        return True
    else: 
        return False

def check_blackjack(deck):
    score=calculate_score(deck)
    if score==21:
        return True
    else:
        return False

        
start = input("Do you want to play a game of Black Jack? y or n: ")
while start=='y':
    user_cards=[]
    computer_cards=[]
    for i in range(0,2):
        deal_cards(user_cards)
        deal_cards(computer_cards)

    user_score = calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)

    # Calculating dist from 21
    user_diff = 21 - user_score
    computer_diff = 21 - computer_score

    print(f"Your cards: {user_cards}, Current score: {user_score}")
    print(f"Dealer's first card: {computer_cards[0]}")
    
    # Checking for Blackjack on first deal or equal score
    if user_score == 21 or computer_score == 21:
            if user_score==21:
                print("You've got a BlackJack")
                print_card()
                print("Congratulation! You Win")
                start=input("Do you want to play again? y or n: ")
                continue
                
            else:
                print("Dealer got a BlackJack")
                print_card()
                print("You Lost, Better luck next time :(")
                start=input("Do you want to play again? y or n: ")
                continue
    elif user_score==computer_score:
        print("Its a Draw")
        start=input("Do you want to play again? y or n: ")
        continue

    # Asking for Hit or Stand
    hit_or_stand = input("Do you want to hit (take one more card) or stand (keep your current hand)?\n")

    # All Cases of Stand
    if hit_or_stand == 'stand':
        stand(user_diff, computer_diff)
        start=input("Do you want to play again? y or n: ")
        continue

    elif hit_or_stand == 'hit':
        while hit_or_stand == 'hit':
            user_cards.append(random.choice(cards))
            user_score = sum(user_cards)

            if computer_score<17:
                computer_cards.append(random.choice(cards))
                computer_score = sum(computer_cards)
            print(f"Your cards: {user_cards}, Score: {user_score}")
            print(f"Dealer's first card: {computer_cards[0]}")

            # Checking for Bust 
            if user_score > 21 or computer_score > 21:
                if user_score > 21:
                    print("Bust!!")
                    print_card()
                    print("Better luck next time")
                    start=input("Do you want to play again? y or n: ")
                    break
                else:
                    print("Dealer Busted")
                    print_card()
                    print("Congratulation! You Win")
                    start=input("Do you want to play again? y or n: ")
                    break

            # Checking for Black Jack
            elif user_score == 21 or computer_score == 21:
                if user_score==21:
                    print("You've got a BlackJack")
                    print("Congratulation! You Win")
                    start=input("Do you want to play again? y or n: ")
                    break
                else:
                    print("Dealer got a BlackJack")
                    print("Better luck next time")
                    start=input("Do you want to play again? y or n: ")
                    break
            
            hit_or_stand = input("Do you want to hit (take one more card) or stand (keep your current hand)?\n")