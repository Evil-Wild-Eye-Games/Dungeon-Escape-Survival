import time, random, webbrowser
#----Above this line is our imports.----
groupname = "\nEvil Wild Eye Games\n"
gamebuild = "\nCurrent Build: A-0.0.107"
debug = True
debug_disabled_msg = "\nDebugging Tools are disabled."
money = random.randint (400,9999) #----The player will recive a random amunt of gold that is specified in the range. The gold will be used to buy various items in the game to help the player along their adventures.
storelist = ["Sword", "Healing Potion", "Speed Potion", "Damage Potion"] #----This will contain items that our player will purchase to help them on their journey. Items in this list are placeholders for now.----
player_inventory = [] #----This will contain the player inventory, items will be added or removed throughout the game----
player_objectives = ["Find the store", "Purchase a weapon from the store", "Purchase a potion from the store"] #----Contains Objectives for the player to complete----
player_completed_objectives = []
player_completed_objective_statement = "has been completed!"
direction_n_count = 0 #----Counts how many times you go North----
direction_s_count = 0 #----Counts how many times you go South----
direction_e_count = 0 #----Counts how many times you go East----
direction_w_count = 0 #----Counts how many times you go West----
travel = True #----When set to True the player can move around the world that they can't even see----
travel_history = [] #----Stores the players travel history----
store = False #----When set to True the player can access the store----
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
unreconized_statement = "\nI couldn't reconize your input. Try Again!"
broke_message = "\nYour too broke for this!"
store_chosen_item = "\nYou chose: A"
store_confimination_item_purchase_question = "are you sure that you want to buy this item?"
store_confirm_item_selection = "\nPlease press 0 to confirm your selection or press any other number to select a different item: "
store_item_purchased = "\nYou have confimed the purchase of"
money_left_1 = "You have"
money_left_2 = "Dollars left to spend. If you need more, continue on your journey."
store_selection_return = "\nReturning to the store selection."
direction_going = "\nYour going"
x = 0 #----East and West coordinates----
y = 0 #----North and South coordinates----
store_location_x = random.randint (-5, 5)
store_location_y = random.randint (-5, 5)
store_location = (store_location_x, store_location_y)
store_found_message = "\nYou have found the store!\n"
enter_key_message = "\nPress Enter to continue."
monster_location_x_1 = random.randint (6, 10)
monster_location_y_1 = random.randint (6, 10)
monster_location_1 = (monster_location_x_1, monster_location_y_1)
monster_location_x_2 = random.randint (8, 14)
monster_location_y_2 = random.randint (8, 14)
monster_location_2 = (monster_location_x_2, monster_location_y_2)
#----Main Variables are above this line.----
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
#----Above this line is the Evil Wild Eye Games Logo for the moment, on the other hand the other logo was too advanced for the Ascii Art that was made.----
time.sleep(2) #----Pauses the program for a number of specified seconds before continuing to execute----
print(groupname) #----Group name prints here----
time.sleep(2) #----Pauses the program for a number of specified seconds before continuing to execute----
print("""  ____                                       _____                            ____                   _            _      _    _       _           
 |  _ \ _   _ _ __   __ _  ___  ___  _ __   | ____|___  ___ __ _ _ __   ___  / ___| _   _ _ ____   _(_)_   ____ _| |    / \  | |_ __ | |__   __ _ 
 | | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \  |  _| / __|/ __/ _` | '_ \ / _ \ \___ \| | | | '__\ \ / / \ \ / / _` | |   / _ \ | | '_ \| '_ \ / _` |
 | |_| | |_| | | | | (_| |  __/ (_) | | | | | |___\__ \ (_| (_| | |_) |  __/  ___) | |_| | |   \ V /| |\ V / (_| | |  / ___ \| | |_) | | | | (_| |
 |____/ \__,_|_| |_|\__, |\___|\___/|_| |_| |_____|___/\___\__,_| .__/ \___| |____/ \__,_|_|    \_/ |_| \_/ \__,_|_| /_/   \_\_| .__/|_| |_|\__,_|
                    |___/                                       |_|                                                            |_|                """)
#----Game name goes above this line inside of the print command.----
time.sleep(2) #----Pauses the program for a number of specified seconds before continuing to execute----
while True: #----This while loop will keep the game alive & run until is told to stop. Also below this line there is a menu system & character selection system----
    menu = int(input("\nWelcome to Dungeon Escape Survival Alpha!\n\nType in 1 to start the game.\nType in 2 to use cheats.\nType in 3 for help.\nType in 4 to view the game build information.\nType in 5 to stop the game.\n\nYour choice goes here: "))
    if menu == 1: #----Game Start----
        print("\nLoading...")
        time.sleep(1) #----Pauses the program for a number of specified seconds before continuing to execute----
        #----Dale start the story from this line----
        time.sleep(0) #----Pauses the program for a number of specified seconds before continuing to execute----
        if travel == False:
            print("\nYou can't travel right now!\n")
            time.sleep(2)
        while travel == True: #----This will run after the player has selected a character----
            if debug == True: #----This will be deleted later and will be used for debugging----
                print("Location of store: ", store_location)
                print("Monster 1:", monster_location_1, "Monster 2:", monster_location_2)
                time.sleep(1.5)
            else:
                print(debug_disabled_msg)
                time.sleep(1)
            travel_direction_count = [direction_n_count, "North", direction_s_count, "South", direction_e_count, "East", direction_w_count, "West"] #----Stores the players current travel session----
            player_location = (x, y)
            print("\nYou are at coordinates", player_location)
            if player_location == store_location:
                print(store_found_message)
                time.sleep(1)
                if player_objectives[0] == "Find the store":
                    del player_objectives[0]
                    player_completed_objectives.append("Find the store")
                    print(player_completed_objectives[0], player_completed_objective_statement)
                if store == False:
                    print("The store is closed.")
                    player_input = int(input("\nThe store is disabled! Do you want to enable the store angain? Press 1 to use the store or 2 to keep the store disabled: "))
                    if player_input == 1:
                        print("\nOpening the store...")
                        store = True
                        break
                    elif player_input == 2:
                        print("\nYou have decided not to shop.")
                    else:
                        print(unreconized_statement)
            if player_location == monster_location_1: #----Runs when the player is on the coordinates of the monster----
                print("\nYou have encountered monster 1")
            elif player_location == monster_location_2:
                print("\nYou have encountered monster 2")
            direction_input = str(input("\nDo you want to move North, South, East, or West?\nTo move North press W\nTo move South press S\nTo move East press D\nTo move West press A\nTo visit the player menu where you can see your Travel History, Player Inventory and etc type in PM.\nTo stop traveling type in Stop.\nType in your choice here: "))
            if direction_input == "W":
                print(direction_going, "North")
                y += 1
                travel_history.append("North")
                direction_n_count += 1
                time.sleep(1.5)
            elif direction_input == "S":
                print(direction_going, "South")
                y -= 1
                travel_history.append("South")
                direction_s_count += 1
                time.sleep(1.5)
            elif direction_input == "D":
                print(direction_going, "East")
                x += 1
                travel_history.append("East")
                direction_e_count += 1
                time.sleep(1.5)
            elif direction_input == "A":
                print(direction_going, "West")
                x -= 1
                travel_history.append("West")
                direction_w_count += 1
                time.sleep(1.5)
            elif direction_input == "PM":
                player_menu = str(input("\nType in TH to view your travel history.\nType in TDC to view the direction count.\nYou can also look at your inventory by typing in PIN.\nType in your choice here: "))
                if player_menu == "TH":
                    print("Travel History: ", travel_history)
                    enter_input = str(input(enter_key_message))
                elif player_menu == "TDC":
                    print("Travel Direction Count: ", travel_direction_count)
                    enter_input = str(input(enter_key_message))
                elif player_menu == "PIN":
                    print("Your inventory: ", player_inventory)
                    enter_input = str(input(enter_key_message))
            elif direction_input == "Stop":
                print("\nYou have decided to stop traveling...")
                time.sleep(0.5)
                break
            else:
                print(unreconized_statement, "\nDid you capitalize the letter or make a typo?")
                time.sleep(2)
        while store == True: #---The store will now be here within this while loop----
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
                store = False
                time.sleep(2)
                break
            else: #----Runs when nothing else matches any statement specified with numbers in this case with the store----
                print("\nThe item specified doesn't exist.")
                time.sleep(2)
        #----AMR program Weapon Stats here----
        #----AMR program Player HP here----
        #----AMR program Winning & Dying here----
    elif menu == 2: #----Cheats for giggles----
        print("\nHaha, there are no cheats!")
        time.sleep(2) #----Pauses the program for a number of specified seconds before continuing to execute----
    elif menu == 3: #----Sends the player to our help page----
        webbrowser.open_new_tab("https://trello.com/b/RFJlZLU6/dungeon-escape-survival-trello")
        time.sleep(6)
        webbrowser.open_new_tab("https://github.com/DamienM2004/Evil-Wild-Eye-Games")
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