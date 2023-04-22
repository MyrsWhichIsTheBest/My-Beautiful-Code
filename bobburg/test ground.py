def price(array, reference):
    total = 0
    for items in range(len(array)):
        total += reference[array[items]]
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
menu_log = {
    "VALUE": ["Beef Burger", "Regular Fries", "Regular Drink"],
    "CHEESY": ["Cheeseburger", "Regular Fries", "Regular Drink"],
    "SUPER": ["Cheeseburger", "Large Fries", "Smoothie"]
}


