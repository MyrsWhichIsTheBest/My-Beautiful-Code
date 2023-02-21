import statistics


def int_check(number):
    try:
        print(int(number))
    except:
        if number != "x":
            return False
    return True


# declaring variables
people = {
}
abs_number = None
list_MostAbs = []
list_NoAbs = []

# inputting the people into 2 separate lists because I need more list practice (also, so I can use .statistics)
while True:
    name = input("Name: ")
    while not int_check(abs_number):
        abs_number = input("Absences: ")
    if abs_number == "x":
        people[-1] = None
        break
    people.update({name: abs_number})
    abs_number = None
print(list_MostAbs)
print(people)


print(f"Average Numbers of Absences: {statistics.mean(people.values())} days\n"
      f"The Most Absences: {max(people.values())}\n"
      f"List of People who were NOT Absent at all: {min(people.values())}")
# i spent 4 hours doing this and it doesnt even work
