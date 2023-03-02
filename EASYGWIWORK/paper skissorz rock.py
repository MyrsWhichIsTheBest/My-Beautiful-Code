import random
import easygui


def psr_game(player):
    result_table = ["Rock", "Scissors", "Paper"]
    number = random.randint(0, 2)
    if player == result_table[number]:
        easygui.msgbox(f"you tied. {result_table[number]}")
    else:
        if player == result_table[number-1]:
            easygui.msgbox(f"you win. {result_table[number]}")
        else:
            easygui.msgbox(f"you lose. {result_table[number]}")


while True:
    psr_game(easygui.buttonbox("choose", choices=["Rock", "Paper", "Scissors"]))
