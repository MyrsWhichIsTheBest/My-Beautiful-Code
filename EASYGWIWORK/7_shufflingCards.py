import random
import easygui


def translate_cards(card_name):
    if card_name[0] == 1:
        return "Ace of" + card_name[1]
    elif card_name[0] <= 10:
        return str(card_name[0]) + " of " + card_name[1]
    else:
        if card_name[0] == 11:
            return "Jack of " + card_name[1]
        elif card_name[0] == 12:
            return "Queen of " + card_name[1]
        else:
            return "King of " + card_name[1]


def replace_empty(replacer):
    pass


deck = []
hand = []
formatted_hand = []
empty_string = "Your Cards: \n"
suits = ["Diamonds", "Clubs", "Spades", "Hearts"]
cards = 13
for card_loop in range(cards):
    for i in range(len(suits)):
        deck.append([card_loop + 1, suits[i]])

print(deck)
draw = easygui.integerbox("How many cards (MAX 52 CARDS)")

random.shuffle(deck)
for i in range(draw):
    while True:
        try:
            if deck[i] != "empty":
                hand.append(deck.pop(i))
                deck.insert(i, "empty")
                break
        except:
            easygui.exceptionbox("Too Many Cards Requested!")
            raise Exception()

for i in range(len(hand)):
    empty_string += " *  " + translate_cards(hand[i]) + "\n"

easygui.msgbox(empty_string)
