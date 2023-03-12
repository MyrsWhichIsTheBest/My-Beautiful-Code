import easygui


list_form = "Here's the list: \n"
inputs = easygui.enterbox("enter the names of 5 places you would like to visit. separate each place name with a comma").split(",")
for i in range(len(inputs)):
    list_form = list_form + " * " + inputs[i].strip() + "\n"
while True:
    if easygui.buttonbox(list_form, choices=["OK", "Edit"]) == "Edit":
        c = easygui.choicebox("Choose what you want to edit:", choices=inputs)
        x = easygui.enterbox("What would you like to change to?")
        list_form = list_form.replace(c, x)
        inputs[inputs.index(c)] = x
    else:
        break


