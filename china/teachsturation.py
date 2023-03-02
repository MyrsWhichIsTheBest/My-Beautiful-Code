import easygui
import math


while True:
    school = easygui.enterbox("Enter name of school")
    max_stu = easygui.integerbox("What is the maximum number of children allowed per class?")
    total_stu = easygui.integerbox(f"What is the total number of children at {school}?\n"
                                   f"Note: Must be between 10 and 9999",
                                   upperbound=9999, lowerbound=10)
    total_teachers = easygui.integerbox("What is the total amount of teachers? \n", upperbound=9999)
    if math.ceil(total_stu / max_stu) < total_teachers:
        easygui.msgbox(f"You have too many teacher/s \n"
                       f"\n"
                       f"Required Teachers {math.ceil(total_stu / max_stu)}\n"
                       f"Current Teachers {total_teachers}")
    elif math.ceil(total_stu / max_stu) > total_teachers:
        easygui.msgbox(f"You have too few teacher/s \n"
                       f"\n"
                       f"Required Teachers: {math.ceil(total_stu / max_stu)}\n"
                       f"Current Teachers: {total_teachers}")
    else:
        easygui.msgbox(f"You have the correct amount of teachers \n"
                       f"\n"
                       f"Required Teachers {math.ceil(total_stu / max_stu)}\n"
                       f"Current Teachers {total_teachers}")
    if easygui.buttonbox("Do another calculation?", choices=["Yes", "No"]) == "No":
        break
