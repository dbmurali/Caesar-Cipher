from art import logo
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(logo)
bidding = {}

continue_bid = True
max_val = 0
winner = ""

while continue_bid == True:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: "))
    bidding[name] = price
    bid_again = input('Enter "y" for continue bidding and "n" for end bit: ')
    print("\n" * 100)
    if bid_again != "y":
        continue_bid = False
        print(bidding)

        for key in bidding:
            if max_val < bidding[key]:
                max_val = bidding[key]
                winner = key
print(F'THE Winner is  "{winner}" with bidding of  "{max_val}" ')

