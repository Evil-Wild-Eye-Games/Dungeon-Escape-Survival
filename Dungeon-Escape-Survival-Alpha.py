import time, random, webbrowser
#----Above this line is our imports.----

groupname = "\nEvil Wild Eye Games\n"
gamebuild = "\nCurrent Build: A-0.0.197"
debug = False
debug_enabled_msg = "\nDebugging Tools are Enabled."
debug_disabled_msg = "\nDebugging Tools are Disabled."
enter_key_message = "\nPress Enter to continue."
unreconized_statement = "\nI couldn't reconize your input. Try Again!"
stupid_error_msg = "\nThis is stupid but, the code didn't work?"
game_items_roster = ["Sword", "Healing Potion", "Speed Potion", "Damage Potion", "Stick"]
pile_msg_1 = "\nYou got a "
pile_msg_2 = " from the pile!"
cell = False
continue_key = 0
#----Info Variables----

money = random.randint (400,9999) #----The player will recive a random amunt of gold that is specified in the range. The gold will be used to buy various items in the game to help the player along their adventures.
player_inventory = [] #----This will contain the player inventory, items will be added or removed throughout the game----
player_objectives = ["Find the store", "Purchase a weapon from the store", "Purchase a potion from the store"] #----Contains Objectives for the player to complete----
player_completed_objectives = []
player_completed_objective_statement = "has been completed!"
#----Player related variables----

storelist = ["Sword", "Healing Potion", "Speed Potion", "Damage Potion"] #----This will contain items that our player will purchase to help them on their journey. Items in this list are placeholders for now.----
store_total_items_counter = 0 #----This value is set to 0 until items are purchased from the shop by the player----
store_purchase_history = [] #----Stores the players purchase history in the game----
slot_0 = 0 #----Set to 0 until this item is bought----
slot_0_cost = 200
slot_0_info = "\n\nThis item can be used to fight monsters with."
slot_1 = 0 #----Set to 0 until this item is bought----
slot_1_cost = 150
slot_1_info = "\n\nThis item can be used to heal your health."
slot_2 = 0 #----Set to 0 until this item is bought----
slot_2_cost = 230
slot_2_info = "\n\nThis item gives you a speed boost for a short amount of time."
slot_3 = 0 #----Set to 0 until this item is bought----
slot_3_cost = 260
slot_3_info = "\n\nThis item make you deal more damage than usual against monsters for a short amount of time."
item_cost_statement = "This item costs: "
broke_message = "\nYour too broke for this!"
store_chosen_item = "\nYou chose: A"
store_confimination_item_purchase_question = "are you sure that you want to buy this item?"
store_confirm_item_selection = "\nPlease press 0 to confirm your selection or press any other number to select a different item: "
store_item_purchased = "\nYou have confimed the purchase of"
money_left_1 = "You have"
money_left_2 = "Dollars left to spend. If you need more, continue on your journey."
store_selection_return = "\nReturning to the store selection."
store_found_message = "\nYou have found the store!\n"
#----Store related variables----

direction_n_count = 0 #----Counts how many times you go North----
direction_s_count = 0 #----Counts how many times you go South----
direction_e_count = 0 #----Counts how many times you go East----
direction_w_count = 0 #----Counts how many times you go West----
travel_history = [] #----Stores the players travel history----
direction_going = "\nYour going"
hallway_number = 0
hallway_msg_1 = "\nYou are now going to go through the "
hallway_msg_2 = " hallway. You can't turn back as the hallway doors have closed upon enterence."
curent_hallway = [] #----Holds the curent hallway name----
#----Travel Related Variables----

weapon_selection_defult_statement = "You have selected a"
weapon_selection_defult_statement_2 = "to use during this battle!"
weapon_selection_error_statement = "You don't have a"
weapon_selection_error_statement_2 = "in your inventory or you chose the wrong slot!"
weapon_slot_1 = "\nChose the slot where your "
weapon_slot_2 = " exists: "
#----Weapon Related Variables----

#----End of Beginning Variables----

def monster_battle(): #----Planned to be redone----
    global game_items_roster, player_inventory, weapon_slot
    while True:
        user_weapon_select = int(input("Which weapon do you want to use for battle?\n\n1: Sword\n\nChoose your weapon: "))
        print("Your inventory:", player_inventory)
        if user_weapon_select == 1:
            weapon_slot = int(input(weapon_slot_1 + game_items_roster[0] + weapon_slot_2))
            if player_inventory[weapon_slot] == "Sword":
                print("\nItem was found!")
                time.sleep(2)
            else:
                print("\nSomething went wrong.")
                if player_inventory == "Sword":
                    print(weapon_selection_defult_statement, game_items_roster[0], weapon_selection_defult_statement_2)
                    time.sleep(4)
                elif player_inventory != "Sword":
                    print(weapon_selection_error_statement, game_items_roster[0], weapon_selection_error_statement_2)
                    time.sleep(2)
                else:
                    print("\nThat option doesn't exist yet!")
                    time.sleep(2)
        else:
            print(unreconized_statement)
def win():
    print("\nCongratulations you win!")
def die():
    print("\nOh no you died! ):")
    user_c_input = str(input("\nDo you want to continue?\n"))
    if user_c_input == "Yes" or user_c_input == "yes" or user_c_input == "Y" or user_c_input == "y":
        print("\nYou have decided to brush yourself off and try again.")
        time.sleep(2)
        return "Continue"
    elif user_c_input == "No" or user_c_input == "no" or user_c_input == "N" or user_c_input == "n":
        print("\nYou have decided to give up on yourself.")
        time.sleep(2)
        return "End Game"
def travel():
    global direction_n_count, direction_s_count, direction_e_count, direction_w_count, enter_input
    direction_input = str(input("\nDo you want to move North, South, East, or West?\n\nTo move North press W\nTo move South press S\nTo move East press D\nTo move West press A\nType in Stop to return the the menu.\n\nType in your choice here: "))
    if direction_input == "W" or direction_input == "w":
        print(direction_going, "North")
        travel_history.append("North")
        time.sleep(1.5)
        return "North"
    elif direction_input == "S" or direction_input == "s":
        print(direction_going, "South")
        travel_history.append("South")
        time.sleep(1.5)
        return "South"
    elif direction_input == "D" or direction_input == "d":
        print(direction_going, "East")
        travel_history.append("East")
        time.sleep(1.5)
        return "East"
    elif direction_input == "A" or direction_input == "a":
        print(direction_going, "West")
        travel_history.append("West")
        time.sleep(1.5)
        return "West"
    elif direction_input == "Stop":
        print("\nReturning to the Main Menu...")
        time.sleep(1.5)
        return "Main Menu"
    else:
        print(unreconized_statement, "\nDid you capitalize the letter or make a typo?")
        time.sleep(2)
def store():
    global money, slot_0, slot_1, slot_2, slot_3, store_total_items_counter, enter_input
    while True:
        print("Money you currently have: ", money)
        print("Items in your inventory: ", player_inventory)
        print("Items in the store: ", storelist)
        store_item_purchased_count = [slot_0, storelist[0], slot_1, storelist[1], slot_2, storelist[2], slot_3, storelist[3]]
        print("Number of each item purchased: ", store_item_purchased_count)
        store_input = int(input("\nEnter a number from 0 - 3 to buy items from the store.\nEnter number 98 to view your in game purchase history.\nEnter number 99 to leave the store.\nGive me a number: "))
        if store_input == 0:
            print(store_chosen_item, storelist[0], store_confimination_item_purchase_question, item_cost_statement, slot_0_cost, slot_0_info)
            storeselect_confirm = int(input(store_confirm_item_selection))
            if storeselect_confirm == 0:
                if money < slot_0_cost:
                    print(broke_message) 
                    time.sleep(2)
                elif money >= slot_0_cost:
                    money -= slot_0_cost
                    print(store_item_purchased, storelist[0], money_left_1, money, money_left_2)
                    store_total_items_counter += 1 #----This adds 1 to the shop selection variable so when the loop tries to run again, it will stop----
                    slot_0 += 1
                    store_purchase_history.append(storelist[0])
                    player_inventory.append(storelist[0])
                    time.sleep(2)
            else:
                print(store_selection_return)
                time.sleep(2)
        elif store_input == 1:
            print(store_chosen_item, storelist[1], store_confimination_item_purchase_question, item_cost_statement, slot_1_cost, slot_1_info)
            shopselect_confirm = int(input(store_confirm_item_selection))
            if shopselect_confirm == 0:
                if money < slot_1_cost:
                    print(broke_message) 
                    time.sleep(2)
                elif money >= slot_1_cost:
                    money -= slot_1_cost
                    print(store_item_purchased, storelist[1], money_left_1, money, money_left_2)
                    store_total_items_counter += 1 #----This adds 1 to the shop selection variable so when the loop tries to run again, it will stop----
                    slot_1 += 1
                    store_purchase_history.append(storelist[1])
                    player_inventory.append(storelist[1])
                    time.sleep(2)
            else:
                print(store_selection_return)
                time.sleep(2)
        elif store_input == 2:
            print(store_chosen_item, storelist[2], store_confimination_item_purchase_question, item_cost_statement, slot_2_cost, slot_2_info)
            shopselect_confirm = int(input(store_confirm_item_selection))
            if shopselect_confirm == 0:
                if money < slot_2_cost:
                    print(broke_message) 
                    time.sleep(2)
                elif money >= slot_2_cost:
                    money -= slot_2_cost
                    print(store_item_purchased, storelist[2], money_left_1, money, money_left_2)
                    store_total_items_counter += 1 #----This adds 1 to the shop selection variable so when the loop tries to run again, it will stop----
                    slot_2 += 1
                    store_purchase_history.append(storelist[2])
                    player_inventory.append(storelist[2])
                    time.sleep(2)
            else:
                print(store_selection_return)
                time.sleep(2)
        elif store_input == 3:
            print(store_chosen_item, storelist[3], store_confimination_item_purchase_question, item_cost_statement, slot_3_cost, slot_3_info)
            shopselect_confirm = int(input(store_confirm_item_selection))
            if shopselect_confirm == 0:
                if money < slot_3_cost:
                    print(broke_message) 
                    time.sleep(2)
                elif money >= slot_3_cost:
                    money -= slot_3_cost
                    print(store_item_purchased, storelist[3], money_left_1, money, money_left_2)
                    store_total_items_counter += 1 #----This adds 1 to the shop selection variable so when the loop tries to run again, it will stop----
                    slot_3 += 1
                    store_purchase_history.append(storelist[3])
                    player_inventory.append(storelist[3])
                    time.sleep(2)
            else:
                print(store_selection_return)
                time.sleep(2)
        elif store_input == 98:
            print("Purchase History: ", store_purchase_history)
            enter_input = str(input(enter_key_message))
        elif store_input == 99:
            print("\nYou are now leaving the store...")
            time.sleep(2)
            break
        else: #----Runs when nothing else matches any statement specified with numbers in this case with the store----
            print("\nThe item specified doesn't exist.")
            time.sleep(2)
def loot_pile():
    rand_item = random.randint(1,23)
    while True:
        if rand_item == 0:
            print("\nHaha! You get nothing!")
            time.sleep(4)
            break
        elif rand_item >= 1 and rand_item <= 6:
            player_inventory.append(game_items_roster[4])
            print(pile_msg_1 + game_items_roster[4] + pile_msg_2)
            time.sleep(4)
            break
        elif rand_item >= 7 and rand_item <= 10:
            player_inventory.append(game_items_roster[1])
            print(pile_msg_1 + game_items_roster[1] + pile_msg_2)
            time.sleep(4)
            break
        elif rand_item >= 11 and rand_item <= 15:
            player_inventory.append(game_items_roster[2])
            print(pile_msg_1 + game_items_roster[2] + pile_msg_2)
            time.sleep(4)
            break
        elif rand_item >= 16 and rand_item <= 21:
            player_inventory.append(game_items_roster[3])
            print(pile_msg_1 + game_items_roster[3] + pile_msg_2)
            time.sleep(4)
            break
        elif rand_item >= 22 and rand_item <= 23:
            player_inventory.append(game_items_roster[0])
            print(pile_msg_1 + game_items_roster[0] + pile_msg_2)
            time.sleep(4)
            break
        else:
            print(stupid_error_msg)
            time.sleep(2)
def someone_is_coming_for_you():
    while True:
        user_dec = int(input("\nYou hear footsteps from down the hall. What will you do?\n\n1: Get out of sight\n2: Stay in sight\n\nYour action: "))
        if user_dec == 1:
            print("\nYou have managed to get out of sight.")
            time.sleep(3)
            return "Safe"
        elif user_dec == 2:
            print("\nYou were spotted and sent back to your cell....")
            time.sleep(3)
            return "Cell"
        else:
            print(unreconized_statement)
            time.sleep(2)
#----End Functions----
print("""????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
???????????????????????????????????JJJJJJY55555555555555555YJJJJJJ??????????????????????????????????
???????????????????????????Y5YPBGGG&&&&&&@@@@@@@@@@@@@@@@@@@&&&&&#GGGB5Y5J?J????????????????????????
???????????????????JYYGP#&#@@@@@@@@@@@@@@@@@@@@@######@@@@@@@@@@@@@@@@@@@&#&BPPYYJ??????????????????
???????????????J5P#&@@@@@@@@@@@@@@@@@@@@@@@@@@P?     .5B@@@@@@@@@@@@@@@@@@@@@@@@@#BPYJ??????????????
???????????J5GB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.        J@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BP5J??????????
????????JPG&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&G5J???????
??????JG&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#PJ?????
????JG&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&P????
???Y#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BY??
??J&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#J?
??B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P?
??B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P?
??5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&Y?
???G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5??
????Y#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#J???
?????J5#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BY?????
????????5#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BY???????
??????????J5G#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:        Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GY??????????
?????????????JJ5G#@@@@@@@@@@@@@@@@@@@@@@@@@@@@.        J@@@@@@@@@@@@@@@@@@@@@@@@@@&BP5J?????????????
??????????????????J5PP##@@@@@@@@@@@@@@@@@@@@@@P7     .YB@@@@@@@@@@@@@@@@@@@@&##PPYJ?????????????????
????????????????????????YYYPGGB&&&&@@@@@@@@@@@@@B#####@@@@@@@@@@@@&&&&BGG5YYJ???????????????????????
???????????????????????????????JJJJY55555GBBBBBBBBBBBBBBBBBP55555Y?JJJ??????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????
????????????????????????????????????????????????????????????????????????????????????????????????????""")
time.sleep(2) #----Pauses the program for a number of specified seconds before continuing to execute----
print(groupname) #----Group name prints here----
time.sleep(2) #----Pauses the program for a number of specified seconds before continuing to execute----
print("""  ____                                       _____                            ____                   _            _      _    _       _           
 |  _ \ _   _ _ __   __ _  ___  ___  _ __   | ____|___  ___ __ _ _ __   ___  / ___| _   _ _ ____   _(_)_   ____ _| |    / \  | |_ __ | |__   __ _ 
 | | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \  |  _| / __|/ __/ _` | '_ \ / _ \ \___ \| | | | '__\ \ / / \ \ / / _` | |   / _ \ | | '_ \| '_ \ / _` |
 | |_| | |_| | | | | (_| |  __/ (_) | | | | | |___\__ \ (_| (_| | |_) |  __/  ___) | |_| | |   \ V /| |\ V / (_| | |  / ___ \| | |_) | | | | (_| |
 |____/ \__,_|_| |_|\__, |\___|\___/|_| |_| |_____|___/\___\__,_| .__/ \___| |____/ \__,_|_|    \_/ |_| \_/ \__,_|_| /_/   \_\_| .__/|_| |_|\__,_|
                    |___/                                       |_|                                                            |_|                """)
time.sleep(2) #----Pauses the program for a number of specified seconds before continuing to execute----
if debug == True:
    print(debug_enabled_msg)
    time.sleep(2)
    #----Code that needs to be debugged can be put into here----
while True: #----This while loop will keep the game alive & run until is told to stop. Also below this line there is a menu system & character selection system----
    menu = int(input("\nWelcome to Dungeon Escape Survival Alpha!\n\nType in 1 to start the game.\nType in 2 to view your inventory.\nType in 3 for help.\nType in 4 to view the game build information.\nType in 5 to stop the game.\n\nYour choice goes here: "))
    if menu == 1: #----Game Start----
        print("\nLoading...\n\nYou are trapped in a Dungeon, you must find your way out of here. But be careful, this place is not safe! Goodluck player.")
        time.sleep(6) #----Pauses the program for a number of specified seconds before continuing to execute----

        while True:
            user_dec = int(input("\nYour in a locked cell in this dungeon with a guard standing next to your cell with a ring of keys, including one to your cell. What are you going to do?\n\n1: Start mocking the guard\n2: Make an attempt to get the keys off of the guard\n3: Do nothing\n\nSo, what will your choice be: "))
            cell = False
            if user_dec == 1:
                print("\nYou have started to mock the guard but, that didn't help you at all since you've angered them.")
                time.sleep(4)
            elif user_dec == 2:
                print("\nYou'll try to take the keys from the guard.")
                time.sleep(2)
                chance = random.randint(0, 1)
                if chance == 0:
                    print("\nNice one! The guard is now unconscious and your able to get out of your cell.")
                    time.sleep(2)
                    print("\nAfter finding stairs and reaching the top of them, you find yourself seeing 4 different hallways but, which one will you take?")
                    time.sleep(4)
                    while True:
                        travel_result = travel() #----This will run the function and take returns if there are any----
                        if travel_result == "North":
                            print("\nNorth is confirmed!") #----Delete this later----
                            hallway_number = 1
                            time.sleep(2)
                            break
                        elif travel_result == "South":
                            print("\nSouth is confirmed!") #----Delete this later----
                            hallway_number = 2
                            time.sleep(2)
                            break
                        elif travel_result == "East":
                            print("\nEast is confirmed!") #----Delete this later----
                            hallway_number = 3
                            time.sleep(2)
                            break
                        elif travel_result == "West":
                            print("\nWest is confirmed!") #----Delete this later----
                            hallway_number = 4
                            time.sleep(2)
                            break
                        elif travel_result == "Main Menu":
                            print("\nReturn to Main Menu is confirmed!") #----Delete this later----
                            time.sleep(2)
                            break
                        else:
                            print(stupid_error_msg)
                            time.sleep(2)
                    while True:
                        if cell == True:
                            break
                        if hallway_number == 1:
                            curent_hallway.append("North")
                            print(hallway_msg_1 + curent_hallway[0] + hallway_msg_2)
                            print("Hallway North Area") #----Delete later----
                            time.sleep(6)
                            while True:
                                user_dec = str(input("\nYou stumble apon a pile of items.\n\nWould you like to look through the pile? "))
                                if user_dec == "Yes" or user_dec == "yes" or user_dec == "Y" or user_dec == "y":
                                    print("\nYou have decided to look through the pile of mysterious things...")
                                    result_loot_pile = loot_pile()
                                    print("Pile Area") #----Delete later----
                                    continue_key = 1
                                elif user_dec == "No" or user_dec == "no" or user_dec == "N" or user_dec == "n":
                                    print("\nYou have decided not to look through the mysterious things.")
                                    print("Pile Area") #----Delete later----
                                    continue_key = 1
                                else:
                                    print(unreconized_statement)
                                    time.sleep(2)
                                if continue_key == 1:
                                    resultchase = someone_is_coming_for_you()
                                    continue_key = 0
                                    if resultchase == "Safe":
                                        print("\nYour safe!")
                                        time.sleep(2)
                                    elif resultchase == "Cell":
                                        cell = True
                                        time.sleep(2)
                                        print("Hide Pile Area") #----Delete later----
                                        break
                        elif hallway_number == 2:
                            curent_hallway.append("South")
                            print(hallway_msg_1 + curent_hallway[0] + hallway_msg_2)
                            time.sleep(6)
                            #----AMR or Dale, please work on the second outcome of the adventure from this statement and must be its own code and not a copy of previous code.----
                            #----However I will allow an exception, You can look at hallway number 1's statement and get an idea on how you will need to structure the other hallways.----
                            #----This doesn't mean copy and pasting line for line, the code must be unique and differentiate from what aleardy exists so the player can experience different outcomes of the adventure.---
                        elif hallway_number == 3:
                            curent_hallway.append("East")
                            print(hallway_msg_1 + curent_hallway[0] + hallway_msg_2)
                            time.sleep(6)
                            #----AMR or Dale, please work on the third outcome of the adventure from this statement and must be its own code and not a copy of previous code.----
                            #----However I will allow an exception, You can look at hallway number 1's statement and get an idea on how you will need to structure the other hallways.----
                            #----This doesn't mean copy and pasting line for line, the code must be unique and differentiate from what aleardy exists so the player can experience different outcomes of the adventure.---
                        elif hallway_number == 4:
                            curent_hallway.append("West")
                            print(hallway_msg_1 + curent_hallway[0] + hallway_msg_2)
                            time.sleep(6)
                            #----AMR or Dale, please work on the fourth outcome of the adventure from this statement and must be its own code and not a copy of previous code.----
                            #----However I will allow an exception, You can look at hallway number 1's statement and get an idea on how you will need to structure the other hallways.----
                            #----This doesn't mean copy and pasting line for line, the code must be unique and differentiate from what aleardy exists so the player can experience different outcomes of the adventure.---
                        else:
                            print(stupid_error_msg)
                            time.sleep(2)

                elif chance == 1:
                    print("\nYou aren't lucky enough.\nThis situation is about to be rougher now.")
                    die_result = die()
                    if die_result == "Continue":
                        print("This should allow the player to continue.") #----Delete this later----
                    elif die_result == "End Game":
                        print("This should end the game.") #----Delete this later----
                        break
            elif user_dec == 3:
                print("You did nothing and you eventually died.")
                time.sleep(4)
                die_result = die()
                if die_result == "Continue":
                    print("This should allow the player to continue.") #----Delete this later----
                elif die_result == "End Game":
                    print("This should end the game.") #----Delete this later----
                    break
            else:
                print(stupid_error_msg)
                time.sleep(2)
    elif menu == 2: #----Player Inventory----
        print("Your inventory:", player_inventory)
        enter_input = str(input(enter_key_message))
    elif menu == 3: #----Sends the player to our help page----
        webbrowser.open_new_tab("https://trello.com/b/RFJlZLU6/dungeon-escape-survival-trello")
        time.sleep(6)
        webbrowser.open_new_tab("https://github.com/Evil-Wild-Eye-Games")
    elif menu == 4:
        print(gamebuild)
        enter_input = str(input(enter_key_message))
    elif menu == 5: #----This stops the game from the menu----
        print("\nStopping game...")
        time.sleep(0.5)
        print("Game has stopped.")
        break
        #----Code that needs to be debugged can be put into here----
    else:
        print(unreconized_statement) #----This will run when the inputted string does not match any of the following statements above.----
        time.sleep(2) #----Pauses the program for a number of specified seconds before continuing to execute----