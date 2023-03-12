import random
import easygui


suits = ["Circls", "squar", "oxygen", "Vaav"]
cards = 13
draw = easygui.integerbox("howmany cards")
show_cards = None

deck = []
for suit in suits:
    for card in range(cards):
        deck.append([card, suit])

random.shuffle(deck)

for item in range(draw):
    show_cards = f"\n*  ".join(deck)

easygui.msgbox(show_cards)
