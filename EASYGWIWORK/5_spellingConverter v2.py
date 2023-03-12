import easygui


while True:
    if easygui.buttonbox("To which language?", choices=["American", "Commonwealth"]) == "American":
        og_word = easygui.enterbox("Choose the word that you wish to translate:")
        word = og_word.lower().strip().replace("our", "or").replace("ise", "ize").replace("yse", "yze")
    else:
        og_word = easygui.enterbox("Choose the word that you wish to translate:")
        word = og_word.lower().strip().replace("or", "our").replace("ize", "ise").replace("yze", "yse")

    if og_word == word:
        easygui.msgbox(f"{word}, No Change In Spelling")
    else:
        easygui.msgbox(word)

    if easygui.buttonbox("Do you wish to translate again?", choices=("Yes", "No")) == "No":
        break

