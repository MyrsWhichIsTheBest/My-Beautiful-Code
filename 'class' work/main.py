import random
import easygui


def conjunct(country, chinese_bool):
    tee = "yet"
    if country.lower() == "china" and chinese_bool:
        tee = "and"
    return tee


class tugBoat:
    def __init__(self, country, chinese):
        self.country = country
        self.chinese = chinese
    x = []
    for i in range(random.randint(1000, 9999)):
        x.append(random.randint(1000, 9999))


p1 = tugBoat(easygui.buttonbox("Where are you from?", choices=["china", "not china"]), easygui.boolbox("You chinese?"))


easygui.msgbox(f"They are from {p1.country} {conjunct(p1.country, p1.chinese)} their chinese value is {p1.chinese}", f"your id is: {tugBoat.x[random.randint(0, 8999)]}")
