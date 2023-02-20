def auction(item, rsv_price):
    # defining variables
    highest_bid = 0
    while highest_bid >= 0:  # I could have used a while true loop
        new_bid = float(input("Bid: "))
        if new_bid > highest_bid and new_bid >= rsv_price:  # checks if the highest bid is less than the new bid and more than the reserve
            highest_bid = new_bid
        elif new_bid == -1:  # if user inputs -1 the program stops the auction
            break
        else:  # if the input does not fit the criteria
            print(f'Bid must be larger than the previous bid (${highest_bid}) and the reserve price (${rsv_price})')
        print(f"The highest bid for {item} is ${highest_bid}")
    return highest_bid


# takes user input and puts them through the function
product = input("Item name: ")
reserve = float(input("Reserve Price: "))
print(f"The Auction has ended!\n"  # prints the ending message
      f"{product} has been sold for {auction(product, reserve)}")
