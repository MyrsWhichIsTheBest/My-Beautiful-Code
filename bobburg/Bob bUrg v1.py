import easygui


class Bob:  # this has class has the Search method which finds and returns the
    def __init__(self, name):
        self.combo = temp_menu[name]
        self.name = name

    def search(self):
        formatted_string = ""  # create empty string
        for food in range(len(self.combo)):
            if food != len(self.combo) - 1:
                # if the item is not the last entry in the list, it will simply add the item to the empty string
                formatted_string += f"{self.combo[food]}, "
            else:  # if the item is last then it will say "and (item)." to make it better for end users and aesthetics
                formatted_string += f"and {self.combo[food]}."
        return [self.combo, f"The {self.name} Meal contains: {formatted_string}", self.name]


def price(name):
    total = 0
    for items in range(len(temp_menu[name])):
        total += dict_of_foods[(temp_menu[name])[items]]
    return total


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
quantity = 0

while True:
    list_of_combos = []
    list_of_food = []

    for key in temp_menu.keys():
        list_of_combos.append(key)

    for key in dict_of_foods.keys():
        list_of_food.append(key)

    print(list_of_food)
    print(list_of_combos)

    option = easygui.buttonbox("What would you like to do?", choices=["Search", "Add", "Delete", "Menu"])  # sends user to correct function
    if option == "Search":
        details = Bob(easygui.enterbox(f"What combo?").upper()).search()  # sends user to Class Bob (at the top)
        price_details = price(details[2].upper())
        easygui.msgbox(details[1] + f"\nWith a total price of: ${price_details}")
    elif option == "Add":
        new_combo_items = []
        combo_name = easygui.enterbox("What do you want to name the combo?").upper()
        while True:
            food_choice = easygui.choicebox("Choose food item:", choices=list_of_food)
            while True:
                if food_choice == "Continue":
                    break
                quantity = easygui.integerbox(f"How many {food_choice}(s)?")
                if quantity >= 0:
                    break
            if dict_of_foods[food_choice] is None:
                break
            for i in range(quantity):
                new_combo_items.append(food_choice)
        if len(new_combo_items) == 0:
            easygui.msgbox("No Changes Made!")
        else:
            if easygui.buttonbox(f"Do you wish to edit this list?\n"
                                 f"{new_combo_items}", choices=["Yes", "No"]) == "Yes":
                print("WIP")
            temp_menu.update({combo_name: new_combo_items})
            print({combo_name: new_combo_items})
    elif option == "Delete":
        temp_menu.pop(easygui.choicebox("What do you want to delete?", list_of_combos))
        # will add extra error control but later
    elif option == "Menu":
        pass
    else:
        raise Exception
