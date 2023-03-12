import random
import easygui


enemyHP = 100
enemyATT = 0
enemyDEF = 6
enemySPD = 0
playerHP = 100
playerATT = 0
playerDEF = 6
playerSPD = 50


plr_abilities = {
    "Damage 15": "15",
    "Speed +": "EFFECT_PSI2",
    "Defence -": "EFFECT_EDD2",
    "Damage 17": "17",
    "kill all men": "99999"
}
enm_abilities = {
    "kill all men": "99999"
}


def player_turn():
    global playerSPD, playerHP, playerDEF, playerATT, enemyDEF, enemyHP, enemySPD, enemyATT
    plr_ability_key = easygui.choicebox("What ability?", "ABILITY", list(plr_abilities.keys()))
    choice = plr_abilities[plr_ability_key]
    enemyPRECALCHP = 0
    if choice[0] == "E":
        effectID = choice[-4:-1]
        effectAMP = int(choice[-1])
        if effectID == "PSI":
            playerSPD += effectAMP
            easygui.msgbox(f"Player's SPD is {playerSPD}")
        elif effectID == "EDD":
            enemyDEF -= effectAMP
            easygui.msgbox(f"Enemy's DEF is {enemyDEF}")
        else:
            easygui.exceptionbox("ID ERROR OCCURRED")
    else:
        if enemySPD * 5 <= random.randint(0, 100):
            enemyPRECALCHP -= int(choice) + playerATT * (random.randint(8, 12)/10)
            if enemyPRECALCHP >= enemyDEF:
                enemyHP -= enemyPRECALCHP
            else:
                enemyHP -= int(choice) + playerATT * (random.randint(8, 12)/10) - enemyDEF
            easygui.msgbox(f"Enemy's HP is {enemyHP}")
        else:
            easygui.msgbox("Attack Missed")


def enemy_turn():
    global playerSPD, playerHP, playerDEF, playerATT, enemyDEF, enemyHP, enemySPD, enemyATT
    enm_ability_key = list(enm_abilities.keys())[random.randint(0, len(enm_abilities)-1)]
    easygui.msgbox(enm_ability_key)
    choice = enm_abilities[enm_ability_key]
    playerPRECALCHP = 0
    if choice[0] == "E":
        effectID = choice[-4:-1]
        effectAMP = int(choice[-1])
        if effectID == "PSI":
            enemySPD += effectAMP
            easygui.msgbox(f"Enemy's SPD is {enemySPD}")
        elif effectID == "EDI":
            playerDEF -= effectAMP
            easygui.msgbox(f"Player's DEF is {playerDEF}")
        else:
            easygui.exceptionbox("ID ERROR OCCURRED")
    else:
        if playerSPD * 5 <= random.randint(0, 100):
            playerPRECALCHP -= int(choice) + enemyATT * (random.randint(8, 12)/10)
            if playerPRECALCHP >= enemyDEF:
                playerHP -= playerPRECALCHP
            else:
                playerHP -= int(choice) + enemyATT * (random.randint(8, 12)/10) - playerDEF
            easygui.msgbox(f"Your HP is {playerHP}")
        else:
            easygui.msgbox("Attack Missed")


while playerHP > 0 or enemyHP > 0:
    player_turn()
    if playerHP < 0 or enemyHP < 0:
        break
    enemy_turn()
    if playerHP < 0 or enemyHP < 0:
        break
