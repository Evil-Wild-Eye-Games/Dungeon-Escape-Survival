import time, random, webbrowser
#----Above this line is our imports.----

groupname = "\nEvil Wild Eye Games\n"
gamebuild = "\nCurrent Build: B-0.1.26\n\nBuild Date: 12/15/2022"
debug = False
debug_enabled_msg = "\nDebugging Tools are Enabled."
debug_disabled_msg = "\nDebugging Tools are Disabled."
enter_key_message = "\nPress Enter to continue."
unreconized_statement = "\nI couldn't reconize your input. Try Again!"
stupid_error_msg = "\nThis is stupid but, the code didn't work?"
game_items_roster = ["Healing Potion", "Speed Potion", "Stick"]
pile_msg_1 = "\nYou got a "
pile_msg_2 = " from the pile!"
cell = 0
pile = 1
win_counter = 0
perm_die_counter = 0
continue_key = 0
#----Info Variables----

money = random.randint (400,9999) #----The player will recive a random amunt of gold that is specified in the range. The gold will be used to buy various items in the game to help the player along their adventures.
player_inventory = [] #----This will contain the player inventory, items will be added or removed throughout the game----
player_objectives = ["Find the store", "Purchase a potion from the store"] #----Contains Objectives for the player to complete----
player_completed_objectives = []
player_completed_objective_statement = "has been completed!"
#----Player related variables----

storelist = ["Healing Potion", "Speed Potion"] #----This will contain items that our player will purchase to help them on their journey. Items in this list are placeholders for now.----
store_total_items_counter = 0 #----This value is set to 0 until items are purchased from the shop by the player----
store_purchase_history = [] #----Stores the players purchase history in the game----
slot_0 = 0 #----Set to 0 until this item is bought----
slot_0_cost = 400
slot_0_info = "\n\nThis item can be used to heal your health."
slot_1 = 0 #----Set to 0 until this item is bought----
slot_1_cost = 600
slot_1_info = "\n\nThis item gives you a speed boost for a short amount of time."
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

travel_history = [] #----Stores the players travel history----
direction_going = "\nYour going"
hallway_number = 0
hallway_msg_1 = "\nYou are now going to go through the "
hallway_msg_2 = " hallway. You can't turn back as the hallway doors have closed upon entrance."
wall_walk_msg = "Dude, you know you can't walk into walls! You're not a ghost like casper so I'm not sure why you did that. Try again! And please don't walk into the wall again. I don't want you to get hurt."
trap_passed_msg = "\nYou have survived the trap!"
trap_wasted_msg = "\nWasted! You have been hit by the trap!"
#----Travel Related Variables----

item_selection_defult_statement = "\nYou have selected a"
item_selection_defult_statement_2 = "to use!"
item_selection_error_statement = "\nYou don't have a"
item_selection_error_statement_2 = "in your inventory or you chose the wrong slot!"
item_slot_1_msg = "\nChose the slot where your "
item_slot_2_msg = " exists: "
#----Item Related Variables----

#----End of Beginning Variables----

def credits():
    print("\nCredits are coming soon! But thanks to you our game will be better on release due to you're feedback!")
def item_selector():
    global game_items_roster, player_inventory
    while True:
        user_item_select = int(input("\nWhich item do you want to use?\n\n1: " + game_items_roster[0] + "\n2: " + game_items_roster[1] + "\n3: " + game_items_roster[2] + "\n\nChoose your item: "))
        print("Your inventory:", player_inventory)
        if user_item_select == 1:
            item_slot = int(input(item_slot_1_msg + game_items_roster[0] + item_slot_2_msg))
            if player_inventory[item_slot] == game_items_roster[0]:
                print("\nItem was found!")
                time.sleep(2)
                print(item_selection_defult_statement, game_items_roster[0], item_selection_defult_statement_2)
                time.sleep(4)
                del player_inventory[item_slot]
                return game_items_roster[0]
            elif player_inventory[item_slot] != game_items_roster[0]:
                print(item_selection_error_statement, game_items_roster[0], item_selection_error_statement_2)
                time.sleep(2)
            else:
                print("\nSomething went wrong. Or that option doesn't exist yet!")
                time.sleep(2)
        elif user_item_select == 2:
            item_slot = int(input(item_slot_1_msg + game_items_roster[1] + item_slot_2_msg))
            if player_inventory[item_slot] == game_items_roster[1]:
                print("\nItem was found!")
                time.sleep(2)
                print(item_selection_defult_statement, game_items_roster[1], item_selection_defult_statement_2)
                time.sleep(4)
                return game_items_roster[1]
            elif player_inventory[item_slot] != game_items_roster[1]:
                print(item_selection_error_statement, game_items_roster[1], item_selection_error_statement_2)
                time.sleep(2)
            else:
                print("\nSomething went wrong. Or that option doesn't exist yet!")
                time.sleep(2)
        elif user_item_select == 3:
            item_slot = int(input(item_slot_1_msg + game_items_roster[2] + item_slot_2_msg))
            if player_inventory[item_slot] == game_items_roster[2]:
                print("\nItem was found!")
                time.sleep(2)
                print(item_selection_defult_statement, game_items_roster[2], item_selection_defult_statement_2)
                time.sleep(4)
                return game_items_roster[2]
            elif player_inventory[item_slot] != game_items_roster[2]:
                print(item_selection_error_statement, game_items_roster[2], item_selection_error_statement_2)
                time.sleep(2)
            else:
                print("\nSomething went wrong. Or that option doesn't exist yet!")
                time.sleep(2)
        else:
            print(unreconized_statement)
            time.sleep(2) 
def win():
    print("\nCongratulations you win!")
    return "Menu"
def die():
    global perm_die_counter
    print("\nOh no you died! ):")
    user_c_input = str(input("\nDo you want to continue?\n\nEnter: Yes, yes, Y, y or No, no, N, n: "))
    if user_c_input == "Yes" or user_c_input == "yes" or user_c_input == "Y" or user_c_input == "y":
        print("\nYou have decided to brush yourself off and try again.")
        time.sleep(2)
        return "Continue"
    elif user_c_input == "No" or user_c_input == "no" or user_c_input == "N" or user_c_input == "n":
        print("\nYou have decided to give up on yourself.")
        time.sleep(2)
        perm_die_counter = 1
        return "End Game"
def travel():
    global enter_input
    direction_input = str(input("\nDo you want to move North, South, East, or West?\n\nTo move North press W\nTo move South press S\nTo move East press D\nTo move West press A\n\nType in your choice here: "))
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
    else:
        print(unreconized_statement, "\nDid you capitalize the letter or make a typo?")
        time.sleep(2)
def store():
    global money, slot_0, slot_1, store_total_items_counter, enter_input
    while True:
        print("Money you currently have: ", money)
        time.sleep(2)
        print("\nItems in your inventory: ", player_inventory)
        print("\nItems in the store: ", storelist)
        store_item_purchased_count = [slot_0, storelist[0], slot_1, storelist[1]]
        print("\nNumber of each item purchased: ", store_item_purchased_count)
        store_input = int(input("\nEnter a number from 0 - 1 to buy items from the store.\nEnter number 98 to view your in game purchase history.\nEnter number 99 to leave the store.\nGive me a number: "))
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
    rand_item = random.randint(0,15)
    while True:
        if rand_item == 0:
            print("\nHaha! You get nothing!")
            time.sleep(4)
            break
        elif rand_item >= 1 and rand_item <= 6:
            player_inventory.append(game_items_roster[0])
            print(pile_msg_1 + game_items_roster[0] + pile_msg_2)
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
        else:
            print(stupid_error_msg)
            time.sleep(2)
def someone_is_coming_for_you():
    while True:
        user_dec = int(input("\nYou hear footsteps from down the hall. What will you do?\n\n1: Get out of sight\n2: Stay in sight\n\nYour action: "))
        if user_dec == 1:
            print("\nYou have managed to get out of sight.")
            time.sleep(2)
            return "Safe"
        elif user_dec == 2:
            print("\nYou were spotted and sent back to you're cell....")
            time.sleep(2)
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
print("""______                                      _____                           _____                  _            _  ______      _        
|  _  \                                    |  ___|                         /  ___|                (_)          | | | ___ \    | |       
| | | |_   _ _ __   __ _  ___  ___  _ __   | |__ ___  ___ __ _ _ __   ___  \ `--. _   _ _ ____   _____   ____ _| | | |_/ / ___| |_ __ _ 
| | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \  |  __/ __|/ __/ _` | '_ \ / _ \  `--. \ | | | '__\ \ / / \ \ / / _` | | | ___ \/ _ \ __/ _` |
| |/ /| |_| | | | | (_| |  __/ (_) | | | | | |__\__ \ (_| (_| | |_) |  __/ /\__/ / |_| | |   \ V /| |\ V / (_| | | | |_/ /  __/ || (_| |
|___/  \__,_|_| |_|\__, |\___|\___/|_| |_| \____/___/\___\__,_| .__/ \___| \____/ \__,_|_|    \_/ |_| \_/ \__,_|_| \____/ \___|\__\__,_|
                    __/ |                                     | |                                                                       
                   |___/                                      |_|                                                                       """)
time.sleep(2) #----Pauses the program for a number of specified seconds before continuing to execute----
if debug == True:
    print(debug_enabled_msg)
    time.sleep(2)
    #----Code that needs to be debugged can be put into here----
while True: #----This while loop will keep the game alive & run until is told to stop. Also below this line there is a menu system & character selection system----
    if win_counter == 1:
        credits()
        time.sleep(6)
        print("\nThanks for playing Dungeon Escape Survival!")
        time.sleep(2)
        break
    if perm_die_counter == 1:
        print("\nBetter luck next time!")
        time.sleep(1)
        break
    menu = int(input("\nWelcome to Dungeon Escape Survival Beta!\n\nType in 1 to start the game.\nType in 2 to view your inventory.\nType in 3 for help.\nType in 4 to view the game build information.\nType in 5 to stop the game.\n\nYour choice goes here: "))
    if menu == 1: #----Game Start----
        print("\nLoading...")
        time.sleep(1.2)
        print("\nYou are trapped in a Dungeon, you must find you're way out of here. But be careful, this place is not safe! Goodluck player.")
        time.sleep(6) #----Pauses the program for a number of specified seconds before continuing to execute----
        while True:
            if win_counter == 1:
                break
            if perm_die_counter == 1:
                break
            cell = 0
            user_dec = int(input("\nYou're in a locked cell in this dungeon with a guard standing next to you're cell with a ring of keys, including one to you're cell. What are you going to do?\n\n1: Start mocking the guard\n2: Make an attempt to get the keys off of the guard\n3: Do nothing\n\nSo, what will your choice be: "))
            if user_dec == 1:
                print("\nYou have started to mock the guard but, that didn't help you at all since you've angered them.")
                time.sleep(2.6)
            elif user_dec == 2:
                print("\nYou'll try to take the keys from the guard.")
                time.sleep(2)
                chance = random.randint(1, 5)
                if chance > 0 and chance <= 3:
                    print("\nNice one! The guard is now unconscious and your able to get out of you're cell.")
                    time.sleep(2)
                    print("\nAfter finding stairs and reaching the top of them, you find yourself seeing 4 different hallways but, which one will you take?")
                    time.sleep(4)
                    while True:
                        travel_result = travel() #----This will run the function and take returns if there are any----
                        if travel_result == "North":
                            hallway_number = 1
                            break
                        elif travel_result == "South":
                            hallway_number = 2
                            break
                        elif travel_result == "East":
                            hallway_number = 3
                            break
                        elif travel_result == "West":
                            hallway_number = 4
                            break
                        else:
                            print(stupid_error_msg)
                            time.sleep(2)
                    while True:
                        if win_counter == 1:
                            break
                        if perm_die_counter == 1:
                            break
                        if cell == 1:
                            break
                        if hallway_number == 1:
                            print(hallway_msg_1 + "North" + hallway_msg_2)
                            time.sleep(6)
                            while True:
                                if win_counter == 1:
                                    break
                                if perm_die_counter == 1:
                                    break
                                if pile == 1:
                                    user_dec = str(input("\nYou stumble apon a pile of items.\n\nWould you like to look through the pile?\n\nEnter: Yes, yes, Y, y, or No, no, N, n: "))
                                    if user_dec == "Yes" or user_dec == "yes" or user_dec == "Y" or user_dec == "y":
                                        time.sleep(4)
                                        print("\nYou have decided to look through the pile of mysterious things...")
                                        result_loot_pile = loot_pile()
                                        continue_key = 1
                                        pile = 0
                                    elif user_dec == "No" or user_dec == "no" or user_dec == "N" or user_dec == "n":
                                        time.sleep(4)
                                        print("\nYou have decided not to look through the mysterious things.")
                                        continue_key = 1
                                        pile = 0
                                    else:
                                        print(unreconized_statement)
                                        time.sleep(2)
                                else:
                                    time.sleep(2)
                                    resultchase = someone_is_coming_for_you()
                                    continue_key = 0
                                    if resultchase == "Safe":
                                        print("\nYou're safe!")
                                        time.sleep(2)
                                        print("\nYou start to see a light to a way out. So you continue forwards...\nYou have found a store!\n\n")
                                        time.sleep(6)
                                        store()
                                        time.sleep(1.2)
                                        print("\nSo you continue after leaving the store with you items, now the only thing left is to get past these traps...\nThere is no going around these traps since its not an option.")
                                        time.sleep(7)
                                        while True:
                                            travel_result = travel() #----This will run the function and take returns if there are any----
                                            if travel_result == "North":
                                                rng_trap = random.randint(1,4)
                                                if rng_trap > 0 and rng_trap <= 3:
                                                    print(trap_passed_msg)
                                                    time.sleep(3)
                                                    travel_result = travel()
                                                    if travel_result == "North":
                                                        time.sleep(1)
                                                        money_grant = random.randint(2,8)
                                                        print("\nYou found" + money_grant + "dollars on the ground!")
                                                        money += money_grant
                                                        time.sleep(2)
                                                        print("\nMoney you currently have: ", money)
                                                        time.sleep(2)
                                                        rng_trap = random.randint(1,4)
                                                        if rng_trap > 0 and rng_trap <= 3:
                                                            print(trap_passed_msg)
                                                            time.sleep(3)
                                                        elif rng_trap == 4:
                                                            print(trap_wasted_msg)
                                                            time.sleep(5)
                                                            item_result = item_selector()
                                                            if item_result == game_items_roster[0]:
                                                                print("\nYou have used a ", game_items_roster[0], " to heal yourself!")
                                                                time.sleep(2)
                                                            else:
                                                                print("Wrong item was selected!\n\nYou have died as a result, you have no chance to try again.")
                                                                perm_die_counter = 1
                                                                break
                                                    #win_result = win()
                                                    #win_counter = 1
                                                    #if win_result == "Menu":
                                                        #break
                                                elif rng_trap == 4:
                                                    print(trap_wasted_msg)
                                                    time.sleep(5)
                                                    item_result = item_selector()
                                                    if item_result == game_items_roster[0]:
                                                        print("\nYou have used a ", game_items_roster[0], " to heal yourself!")
                                                        time.sleep(2)
                                                    else:
                                                        print("Wrong item was selected!\n\nYou have died as a result, you have no chance to try again.")
                                                        perm_die_counter = 1
                                                        break
                                            elif travel_result == "South":
                                                print(wall_walk_msg)
                                                time.sleep(10)
                                            elif travel_result == "East":
                                                print(wall_walk_msg)
                                                time.sleep(10)
                                            elif travel_result == "West":
                                                print(wall_walk_msg)
                                                time.sleep(10)
                                            else:
                                                print(stupid_error_msg)
                                                time.sleep(2)
                                    elif resultchase == "Cell":
                                        cell = 1
                                        time.sleep(2)
                                        break
                                if continue_key == 1:
                                    time.sleep(2)
                                    resultchase = someone_is_coming_for_you()
                                    continue_key = 0
                                    if resultchase == "Safe":
                                        print("\nYou're safe!")
                                        time.sleep(2)
                                        print("\nYou start to see a light to a way out. So you continue forwards...\nYou have found a store!\n\n")
                                        time.sleep(6)
                                        store()
                                        time.sleep(1.2)
                                        print("\nSo you continue after leaving the store with you items, now the only thing left is to get past these traps...\nThere is no going around these traps since its not an option.")
                                        time.sleep(7)
                                        while True:
                                            travel_result = travel() #----This will run the function and take returns if there are any----
                                            if travel_result == "North":
                                                rng_trap = random.randint(1,4)
                                                if rng_trap > 0 and rng_trap <= 3:
                                                    print(trap_passed_msg)
                                                    time.sleep(3)
                                                    travel_result = travel()
                                                    if travel_result == "North":
                                                        time.sleep(1)
                                                        money_grant = random.randint(2,8)
                                                        print("\nYou found" + money_grant + "dollars on the ground!")
                                                        money += money_grant
                                                        time.sleep(2)
                                                        print("\nMoney you currently have: ", money)
                                                        time.sleep(2)
                                                        rng_trap = random.randint(1,4)
                                                        if rng_trap > 0 and rng_trap <= 3:
                                                            print(trap_passed_msg)
                                                            time.sleep(3)
                                                        elif rng_trap == 4:
                                                            print(trap_wasted_msg)
                                                            time.sleep(5)
                                                            item_result = item_selector()
                                                            if item_result == game_items_roster[0]:
                                                                print("\nYou have used a ", game_items_roster[0], " to heal yourself!")
                                                                time.sleep(2)
                                                            else:
                                                                print("Wrong item was selected!\n\nYou have died as a result, you have no chance to try again.")
                                                                perm_die_counter = 1
                                                                break
                                                    #win_result = win()
                                                    #win_counter = 1
                                                    #if win_result == "Menu":
                                                        #break
                                                elif rng_trap == 4:
                                                    print(trap_wasted_msg)
                                                    time.sleep(5)
                                                    item_result = item_selector()
                                                    if item_result == game_items_roster[0]:
                                                        print("\nYou have used a ", game_items_roster[0], " to heal yourself!")
                                                        time.sleep(2)
                                                    else:
                                                        print("Wrong item was selected!\n\nYou have died as a result, you have no chance to try again.")
                                                        perm_die_counter = 1
                                                        break
                                            elif travel_result == "South":
                                                print(wall_walk_msg)
                                                time.sleep(10)
                                            elif travel_result == "East":
                                                print(wall_walk_msg)
                                                time.sleep(10)
                                            elif travel_result == "West":
                                                print(wall_walk_msg)
                                                time.sleep(10)
                                            else:
                                                print(stupid_error_msg)
                                                time.sleep(2)
                                    elif resultchase == "Cell":
                                        cell = 1
                                        time.sleep(2)
                                        break
                        elif hallway_number == 2:
                            print(hallway_msg_1 + "South" + hallway_msg_2)
                            time.sleep(6)
                            #----AMR or Dale, please work on the second outcome of the adventure from this statement and must be its own code and not a copy of previous code.----
                            #----However I will allow an exception, You can look at hallway number 1's statement and get an idea on how you will need to structure the other hallways.----
                            #----This doesn't mean copy and pasting line for line, the code must be unique and differentiate from what aleardy exists so the player can experience different outcomes of the adventure.---
                        elif hallway_number == 3:
                            print(hallway_msg_1 + "East" + hallway_msg_2)
                            time.sleep(6)
                            #----Dale is working on this----
                            #----Dale please work on the third outcome of the adventure from this statement and must be its own code and not a copy of previous code.----
                            #----However I will allow an exception, You can look at hallway number 1's statement and get an idea on how you will need to structure the other hallways.----
                            #----This doesn't mean copy and pasting line for line, the code must be unique and differentiate from what aleardy exists so the player can experience different outcomes of the adventure.---
                        elif hallway_number == 4:
                            print(hallway_msg_1 + "West" + hallway_msg_2)
                            time.sleep(6)
                            #----AMR or Dale, please work on the fourth outcome of the adventure from this statement and must be its own code and not a copy of previous code.----
                            #----However I will allow an exception, You can look at hallway number 1's statement and get an idea on how you will need to structure the other hallways.----
                            #----This doesn't mean copy and pasting line for line, the code must be unique and differentiate from what aleardy exists so the player can experience different outcomes of the adventure.---
                        else:
                            print(stupid_error_msg)
                            time.sleep(2)
                elif chance > 3 and chance <= 5:
                    print("\nYou aren't lucky enough.\nThis situation is about to be rougher now.")
                    die_result = die()
                    if die_result == "Continue":
                        print("")
                    elif die_result == "End Game":
                        break
            elif user_dec == 3:
                print("You did nothing and you eventually died.")
                time.sleep(4)
                die_result = die()
                if die_result == "Continue":
                    continue
                elif die_result == "End Game":
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
    else:
        print(unreconized_statement) #----This will run when the inputted string does not match any of the following statements above.----
        time.sleep(2) #----Pauses the program for a number of specified seconds before continuing to execute----