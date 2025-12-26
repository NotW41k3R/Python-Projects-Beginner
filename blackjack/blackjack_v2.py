import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(reciever):
    return reciever.append(random.choice(cards))

def calculate_score(deck):
    return sum(deck)

def print_card(user_deck, computer_deck):
    user_score = sum(user_deck)
    computer_score = sum(computer_deck)
    print(f"Your final cards: {user_deck}, Final score: {user_score}")
    print(f"Dealer's final cards: {computer_deck}, Final score: {computer_score}")

def stand(user_deck, computer_deck):
    user_diff = 21 - sum(user_deck)
    computer_diff = 21 - sum(computer_deck)

    if user_diff < computer_diff and user_diff > 0:
        print_card(user_deck, computer_deck)
        print("Congratulation! You Win")

    elif user_diff > computer_diff and computer_diff > 0:
        print_card(user_deck, computer_deck)
        print("Better luck next time")

def check_bust(deck):
    score = calculate_score(deck)
    if score > 21:
        while 11 in deck and sum(deck) > 21:
            loc = deck.index(11)
            deck[loc] = 1
    score = calculate_score(deck)
    if score > 21:
        return True
    else:
        return False

def check_blackjack(deck):
    score = calculate_score(deck)
    if score == 21:
        return True
    else:
        return False

def check_draw(user_deck, computer_deck):
    if sum(user_deck) == sum(computer_deck):
        return True
    else:
        return False

def resolve_round(user_deck, computer_deck):
    if check_blackjack(user_deck):
        print("You've got a BlackJack")
        print("Congratulation! You Win")
        return True
    elif check_blackjack(computer_deck):
        print("Dealer got a BlackJack")
        print("You Lost, Better luck next time :(")
        return True
    elif check_bust(user_deck):
        print("Bust!!")
        print("Better luck next time")
        return True
    elif check_bust(computer_deck):
        print("Dealer Busted")
        print("Congratulation! You Win")
        return True
    elif check_draw(user_deck, computer_deck):
        print("Its a Draw")
        return True
    else:
        return False

def dealer_turn(user_deck, computer_deck):
        while sum(computer_deck) < 17:
            deal_cards(computer_deck)
            round_over = resolve_round(user_deck, computer_deck)
            if round_over:
                print_card(user_deck, computer_deck)
                return
        stand(user_deck, computer_deck)
        return

def check_and_end_round(user_deck, computer_deck):
    if resolve_round(user_deck, computer_deck):
        print_card(user_deck, computer_deck)
        return True
    return False

def play():
    print(art.logo)
    round_over = False
    user_cards = []
    computer_cards = []
    for i in range(0, 2):
        deal_cards(user_cards)
        deal_cards(computer_cards)
    while not round_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, Current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if check_and_end_round(user_cards, computer_cards):
            return

        # Asking for Hit or Stand
        hit_or_stand = input("Do you want to hit (take one more card) or stand (keep your current hand)?\n")

        if hit_or_stand == 'stand':
            dealer_turn(user_cards, computer_cards)
            return

        elif hit_or_stand == 'hit':
            while hit_or_stand == 'hit':
                deal_cards(user_cards)
                user_score = calculate_score(user_cards)

                print(f"Your cards: {user_cards}, Score: {user_score}")
                print(f"Dealer's first card: {computer_cards[0]}")

                if check_and_end_round(user_cards, computer_cards):
                    return
                hit_or_stand = input("Do you want to hit (take one more card) or stand (keep your current hand)?\n")
                if hit_or_stand == 'stand':
                    dealer_turn(user_cards, computer_cards)
                    return

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play()