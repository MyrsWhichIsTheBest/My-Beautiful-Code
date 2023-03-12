import random
import easygui


while not easygui.boolbox("exit?"):
    lst = []
    total = 0
    sides = easygui.buttonbox("How many sided die?", choices=["4", "6", "8", "12", "20", "100"])
    for i in range(easygui.integerbox("How many times?")):
        x = random.randint(1, int(sides))
        lst.append(x)
        total += x
    easygui.msgbox(f"You rolled:\n"
                   f"{lst}\n"
                   f"Which totals to: {total}")

