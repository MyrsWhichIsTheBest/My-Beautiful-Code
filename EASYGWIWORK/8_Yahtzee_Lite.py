import random
import easygui


# variables for global
player_1 = easygui.enterbox("What is P1's name")
player_2 = easygui.enterbox("What is P2's name")


def list_formatter(input_list, message):  # formats the list into a nice bullet point string for easyGUI
    empty = message + "\n"  # message is the message printed at the top of the list
    for inputs in range(len(input_list)):
        empty += f" *  {str(input_list[inputs])}\n"
        # loops for the range of the list adding one entry at a time
    return empty


def result_table(input_list, loop_num):  # result_table() takes in the list and finds any matching 3, 4, or 5
    message = ""
    for roll_loop in range(6):
        if input_list.count(roll_loop + 1) >= 5:  # if function finds a 5, 4, or 3, it will exit the loop
            message = f"({roll_loop + 1}) Yahtzee!"
            players[loop_num] = 50
            break
        elif input_list.count(roll_loop + 1) >= 4:
            message = f"({roll_loop + 1}) 4 of a kind!"
            players[loop_num] = 30
            break
        elif input_list.count(roll_loop + 1) >= 3:
            message = f"({roll_loop + 1}) 3 of a kind!"
            players[loop_num] = 10
            break
        if roll_loop == 5:
            message = "Better Luck Next Time!"
    return message


while True:
    # variables
    rolls = 3  # number of times this will be rolled
    players = [player_1, player_2]

    for player in range(2):
        while rolls > 0:
            results = []
            for i in range(5):
                results.append(random.randint(1, 6))

            results.sort()
            print(list_formatter(results, "Numbers rolled:") + "\n")
            if rolls > 1:
                if easygui.buttonbox(list_formatter(results, "Numbers rolled:") + "\n" + result_table(results, player), choices=["Re-roll", "Stick"]) == "Stick":
                    break
                else:
                    rolls -= 1
            else:
                easygui.msgbox(list_formatter(results, "Numbers rolled:") + "\n" + result_table(results, player))
                rolls -= 1

    print(players[0], players[1])

    if players[0] == players[1]:
        easygui.msgbox(f"Draw!")
    else:
        if players[0] < players[1]:
            winner = player_2
        else:
            winner = player_1
        if easygui.buttonbox(f"Player {winner} won! \n Do you want to play another round?", choices=["Yes", "No"]) == "No":
            break
