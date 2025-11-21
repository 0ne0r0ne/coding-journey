name_and_bid = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    case = input("Are there any other bidders? type 'yes' or 'no'.").lower()
    name_and_bid[name] = bid

    if case == 'no':
        case = "no"
        name_last, bid_last = max(name_and_bid.items(), key=lambda x: x[1])
        print(f"The winner is {name_last} with a bid of ${bid_last}")
        break


