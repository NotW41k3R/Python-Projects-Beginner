def clear_console():
    print("\n" * 50)

ascii_art = """
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|
                         ___________
                         \         /
                          )_______(
                          |\"\"\"\"\"\"\"|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )\"\"\"\"\"\"\"(
                         /_________|
                       .------------|
                      /______________|
"""
print(ascii_art)

bid_data={}
again=True
while again:

    name=input("Enter your name: \n")
    bid=int(input("Enter your Bid: \n"))
    bid_data[name]=bid
    anyone=input("Is someone else bidding? y or n\n")
    if anyone=="y":
        again = True
    else:
        again = False
    clear_console()
max_bidder = max(bid_data, key=bid_data.get)
max_bid = bid_data[max_bidder]

print(f"Highest Bidder is {max_bidder} with ${max_bid}")

