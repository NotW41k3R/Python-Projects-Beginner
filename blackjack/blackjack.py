import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start = input("Do you want to play a game of Black Jack? y or n: ")
while start=='y':
    user_cards=[random.choice(cards), random.choice(cards)]
    computer_cards=[random.choice(cards), random.choice(cards)]

    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    print(f"Your cards: {user_cards}, Current score: {user_score}")
    print(f"Dealer's first card: {computer_cards[0]}")
    hit_or_stand = input("Do you want to hit (take one more card) or stand (keep your current hand)?")
    while hit_or_stand == 'hit':
        user_cards.append(random.choice(cards))
        if computer_score<17
        user_score = sum(user_cards)
        print(f"Your final cards: {user_cards}, Final score: {user_score}")
        print(f"Dealer's final cards: {computer_cards}, Final score: {computer_score}")

        if user_score == 21 or computer_score == 21:
            if user_score==21:
                print("You've got a BlackJack")
                print("Congratulation! You Win")
            else:
                print("Dealer got a BlackJack")
                print("Better luck next time")
