import easygui


class Bob:  # this has class has the Search method which finds and returns the
    def __init__(self, name):
        self.name = name

    def search(self):
        formatted_string = ""  # create empty string
        combo = temp_menu[self.name]
        return [combo, f"The {self.name} Meal contains: {arr_format(combo, 'list')}", self.name]

    def add(self):
        new_combo_items = []
        amount = 0
        while True:
            food_choice = easygui.choicebox("Choose food item:", choices=list_of_food)  # maybe add the formatted list under text
            while True:
                if food_choice == "Continue" or None:
                    break
                amount = easygui.integerbox(f"How many {food_choice}(s)?")
                if amount is None:
                    break
                if amount >= 0:
                    break
            if amount is None:
                continue
            if dict_of_foods[food_choice] is None:
                break
            for i in range(amount):
                new_combo_items.append(food_choice)
        if len(new_combo_items) == 0:
            return "Nothing Added"
        else:
            return {self.name: new_combo_items}


def price(name):
    total = 0
    for items in range(len(temp_menu[name])):
        total += dict_of_foods[(temp_menu[name])[items]]
    return total


def arr_format(array, format_option="list", message="", organize=False):
    formatted_string = message + "\n"
    if format_option == "list":
        for items in range(len(array)):
            if items != len(array) - 1:
                # if the item is not the last entry in the list, it will simply add the item to the empty string
                formatted_string += f" -\t{array[items]}\n"
            else:  # if the item is last then it will say "and (item)." to make it better for end users and aesthetics
                formatted_string += f" -\t{array[items]}"
    elif format_option == "line":
        for items in range(len(array)):
            if items != len(array) - 1:
                # if the item is not the last entry in the list, it will simply add the item to the empty string
                formatted_string += f"{array[items]}, "
            else:  # if the item is last then it will say "and (item)." to make it better for end users and aesthetics
                formatted_string += f"and {array[items]}."
    return formatted_string


def multiple_collapse(array, list_or_dict=dict):
    """input a list with multiple values returning the value as a dictionary
    (formatted like: {"item": amount})
    or as a nested list (formatted like: [["item A": amount],["item B": amount]]"""
    organized = {}
    format_list = []
    for item in array:
        if item in organized:
            continue
        format_list.append(f"{item} x{array.count(item)}")
        organized.update({item: array.count(item)})
    if list_or_dict == list:
        return format_list
    else:
        return organized


dict_of_foods = {
    "Continue": None,
    "Beef Burger": 5.69,
    "Cheeseburger": 6.69,
    "Regular Fries": 1,
    "Large Fries": 2,
    "Regular Drink": 1,
    "Large Drink": 2,
    "Smoothie": 2
}
temp_menu = {
    "VALUE": ["Beef Burger", "Regular Fries", "Regular Drink"],
    "CHEESY": ["Cheeseburger", "Regular Fries", "Regular Drink"],
    "SUPER": ["Cheeseburger", "Large Fries", "Smoothie"]
}


while True:
    list_of_combos = []
    list_of_food = []

    for key in temp_menu.keys():
        list_of_combos.append(key)

    for key in dict_of_foods.keys():
        list_of_food.append(key)

    print(list_of_food)
    print(list_of_combos)
    arr_format(list_of_combos, "line")

    option = easygui.buttonbox("What would you like to do?", choices=["Search", "Add", "Delete", "Combos"])  # sends user to correct function
    if option == "Search":
        details = Bob(easygui.choicebox(f"What combo?", choices=list_of_combos)).search()  # sends user to Class Bob's search() method (at the top)
        price_details = price(details[2].upper())  # sends user to function price()
        easygui.msgbox(details[1] + f"\nWith a total price of: ${price_details}")
    elif option == "Add":
        new_entry = Bob(easygui.enterbox("What do you want to name the combo?").upper()).add()  # sends user to Class Bob's add() method (at the top)
        if type(new_entry) is dict:  # check what the returning variable type is
            print("Added New Item(s)!")  # debug
            easygui.msgbox(f"Added {list(new_entry.keys())[0]} Combo!")
            temp_menu.update(new_entry)  # update the menu
        else:
            easygui.msgbox(new_entry)  # print the 'No Changes Made' message
    elif option == "Delete":
        choices = list_of_combos.insert(0, "Cancel")
        delete_thing = easygui.choicebox("What do you want to delete?", choices=choices)  # might not work
        if delete_thing != "Cancel":
            if easygui.ynbox(f"Do you wish to delete {delete_thing}?"):  # error checker
                del temp_menu[delete_thing]
                easygui.msgbox("Deleted Successfully")
            else:
                easygui.msgbox("Canceled Deletion")
        else:
            easygui.msgbox("Canceled Deletion")
    elif option == "Combos":
        easygui.msgbox(arr_format(list_of_combos, 'list', 'The available Combos are: '))
    else:
        raise Exception
