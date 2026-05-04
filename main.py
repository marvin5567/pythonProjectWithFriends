import os
from time import sleep # this is used to create a delay between prints
import art_assets # where all the ascii art is stored

# player variables
inventory = []
name = ""

# game state variables
game_running = False
gameSpeed = 1.5 # this will be used to control how fast text prints

## karim
def save_game(inventory):
    with open("save_data.txt", "w") as file:
        for item in inventory:
            file.write(item + "\n")
    sleep(0.5)
    print("\n>>> GAME SAVED. Your evidence is secure. <<<\n")

def load_game(inventory):
    if os.path.exists("save_data.txt"):
        inventory.clear()
        with open("save_data.txt", "r") as file:
            for line in file:
                inventory.append(line.strip())
        sleep(0.5)
        print("\n>>> GAME LOADED. Welcome back to the investigation. <<<\n")
        return True
    else:
        sleep(0.5)
        print("\n>>> ERROR: No save file exists. <<<\n")
        return False

def settings_menu():
    global gameSpeed
    while True:
        print("================ SETTINGS ================")
        print(f"Current Game Speed: {gameSpeed} seconds per text block.")
        print("[1] Fast (0.5s delay)")
        print("[2] Normal (1.5s delay)")
        print("[3] Slow (2.5s delay)")
        print("[4] Back to Main Menu")
        
        choice = input("Select an option: ")
        if choice == "1":
            gameSpeed = 0.5
            print(">>> Speed set to Fast. <<<")
        elif choice == "2":
            gameSpeed = 1.5
            print(">>> Speed set to Normal. <<<")
        elif choice == "3":
            gameSpeed = 2.5
            print(">>> Speed set to Slow. <<<")
        elif choice == "4":
            print("==================================\n")
            break
        else:
            print("Invalid choice. Try again.")

def start_game():
    global game_running
    game_running = True
    intro()
    while game_running:       
        choice = int(input(f"\n{name} (in your head): Alright, what should I do?\nGo To:\n[1] Roller Coaster \n[2] Arcade \n[3] Canteen \n\nActions:\n[4] View Evidence\n[5] Accuse\n[6] Save Game\n"))     
        if choice == 1:
            coaster_room(inventory)
        elif choice == 2:
            arcade_room(inventory)
        elif choice == 3:
            canteen_room(inventory)
        elif choice == 4:
            view_evidence(inventory)
        elif choice == 5:
            if len(inventory) == 0:
                print("Are you sure about this? You have no evidence to present. Your choice here matters more than you'd know.")
                yesOrno = input("[yes] [no]\n")
                if (yesOrno.lower() == "yes") or (yesOrno.lower() == "y"):
                    game_running = make_accusation(inventory)
                elif (yesOrno.lower() == "no") or (yesOrno.lower() == "n"):
                    print(f"Good choice, {name}. You should gather more evidence before making an accusation.")
            else:
                game_running = make_accusation(inventory)
        elif choice == 6:
            save_game(inventory)

def make_accusation(inventory):
    sleep(gameSpeed)
    print(art_assets.ART_ACCUSE)
    sleep(gameSpeed)
    print("This is it. You've gathered the clues, spoken to the suspects, and the time has come.")
    sleep(gameSpeed)
    print("Who is the killer?")
    print("[1] Bugs Bunny")
    print("[2] The Operator")
    print("[3] The Boyfriend")
    print("[4] Maintenance")
    print("[5] The Janitor")
    
    choice = input("\nEnter the number of the suspect you accuse: ")
    
    if choice == "1":
        sleep(gameSpeed)
        print("\nBugs Bunny looks at you, drops his carrot, and breaks the fourth wall.")
        sleep(gameSpeed)
        print("'Doc, I literally don't have individual fingers to hold a weapon. I'm wearing cartoon gloves!'")
        sleep(gameSpeed)
        print("He laughs at your terrible detective skills and hops away. You are a laughingstock.")
        sleep(gameSpeed)
        print(">>> JOKE ENDING: GAME OVER <<<")
        return False
        
    elif choice == "2":
        sleep(gameSpeed)
        print("\nYou point your finger at the Operator. He gasps, turns pale, and immediately faints from pure terror.")
        sleep(gameSpeed)
        print("While you're waiting for the paramedics to wake him up, the real killer easily slips away.")
        sleep(gameSpeed)
        print(">>> BAD ENDING: WRONG SUSPECT. GAME OVER <<<")
        return False
        
    elif choice == "3":
        sleep(gameSpeed)
        print("\nYou accuse the Boyfriend. He breaks down in tears.")
        sleep(gameSpeed)
        print("Just as you're slapping the cuffs on him, Maintenance bursts in with the arcade token logs, proving the Boyfriend's alibi.")
        sleep(gameSpeed)
        print("You have to let him go, but the actual murderer has already escaped the carnival.")
        sleep(gameSpeed)
        print(">>> BAD ENDING (The Innocent): GAME OVER <<<")
        return False
        
    elif choice == "4":
        sleep(gameSpeed)
        print("\nYou accuse the Maintenance worker. He throws his hands up in panic.")
        sleep(gameSpeed)
        print("'Alright, alright! I stole the arcade tokens! I admit it!'")
        sleep(gameSpeed)
        print("You arrest him for petty theft, but the murder charges don't stick. The real killer walks free.")
        sleep(gameSpeed)
        print(">>> BAD ENDING: WRONG CRIME. GAME OVER <<<")
        return False
        
    elif choice == "5":
        # The ultimate logic check for the True Ending
        if "bloody_pipe" in inventory and "body_moved" in inventory and "janitor_on_tracks" in inventory:
            sleep(gameSpeed)
            print("\nYou corner the Janitor, presenting the bloody pipe from his closet.")
            sleep(gameSpeed)
            print("You recount how he was seen dragging heavy bags, and how he lied about not being on the tracks.")
            sleep(gameSpeed)
            print("The Janitor's eyes go wide. He turns to run, but slips spectacularly on a puddle of spilled soda!")
            sleep(gameSpeed)
            print("He crashes into a trash can and angrily confesses everything in a fit of rage.")
            sleep(gameSpeed)
            print("'Fine! I did it! But she stepped on my freshly mopped floor! Nobody respects the floor!'")
            sleep(gameSpeed)
            print(">>> TRUE ENDING: YOU CAUGHT THE KILLER. YOU WIN! <<<")
            return False
        else:
            sleep(gameSpeed)
            print("\nYou accuse the Janitor. He just stares at you, leaning lazily on his mop.")
            sleep(gameSpeed)
            print("'Yeah? Got any actual proof, detective? Because unless you have something solid, you're just blowing hot air.'")
            sleep(gameSpeed)
            print("Without enough evidence to definitively link him to the weapon, the timeline, and the body, he laughs you out of the room.")
            sleep(gameSpeed)
            print("He gets away with murder.")
            sleep(gameSpeed)
            print(">>> BAD ENDING (Lack of Evidence): GAME OVER <<<")
            return False
            
    else:
        sleep(gameSpeed)
        print("\nInvalid choice. The pressure gets to you, and you pass out. The killer escapes.")
        print(">>> GAME OVER <<<")
        return False

def view_evidence(inventory):
    print(art_assets.ART_EVIDENCE)
    if len(inventory) == 0:
        sleep(0.5)
        print("You have no evidence in your inventory.")
    else:
        sleep(0.5)
        print("You have the following evidence in your inventory:")
        for item in inventory:
            print(f"- {item}")
    print("====================")


def intro():
    global name 
    start_screen = True

    print("================== Murder Mystery ==================")
    print(art_assets.ART_TITLE)
    print("################# Carnival Canaver #################")
    while start_screen:
        choice = int(input("\n[1] New Game\n[2] Continue\n[3] Settings\n[4] Quit\n"))
        if choice == 1:
            inventory.clear()
            start_screen = False
        elif choice == 2:
            if load_game(inventory):
                start_screen = False
        elif choice == 3:
            settings_menu()
        elif choice == 4:
            print("Thanks for playing!")
            exit()
            
    name = input("What is your name, detective? ")
    print(art_assets.ART_COP)
    sleep(gameSpeed)
    print(f"Officer: Welcome, detective {name}! Let me fill you in on the details.")
    sleep(gameSpeed)
    print("Officer: The victim was a woman, aged 22, found dead in trash bags in the canteen.")
    sleep(gameSpeed)
    print("Officer: Witness reports and forensic data suggest that the murder took place in the roller coaster.")
    sleep(gameSpeed)
    print("Officer: On the carnival site, we have five suspects scattered in 3 different areas. Catch that soulless bastard!")
    sleep(gameSpeed)
    print(f"{name}: You can count on me, officer :)")
    sleep(gameSpeed)

## okasha
def canteen_room(inventory):
    sleep(gameSpeed)
    print(art_assets.ART_CANTEEN)
    sleep(gameSpeed)
    print("A messy, brightly lit area. Bugs Bunny and The Janitor are here.")
    while True:
        print("\n[1] Talk to Bugs Bunny")
        print("[2] Talk to The Janitor")
        print("[3] Inspect the Trash Bin")
        print("[4] Leave the Canteen")

        choice = int(input("Enter choice: "))
        if choice == 1 :
            npc_bugs(inventory)
        elif choice == 2 :
            npc_janitor(inventory)
        elif choice == 3 :
            sleep(gameSpeed)
            if "bloody_gloves" not in inventory :
                print("You dig through the bin and find a pair of bloody_gloves!")
                inventory.append("bloody_gloves")
            else :
                print("The bin is empty now.")
        elif choice == 4 :
            break
        else:
            print("Try another choice.")     

def npc_bugs(inventory):
    sleep(gameSpeed)
    print(art_assets.ART_BUGS)
    while True :
        print("\nQ1: What were you doing??")
        print("Q2: Did you see anything out of the ordinary?")
        print("Q3: Have any theories?")
        if "janitor_closet" in inventory:
            print("Q4: Are you sure the Janitor was with you the whole time?")
        print("[5] Leave")

        choice = int(input("Select a question to ask Bunny or leave(5): "))
        if choice == 1:
            sleep(gameSpeed)
            print("\nBugs: 'Oh, howdy pal! I was just entertaining the kiddos over by the prize booth! My buddy the Janitor was right next to me!'")
        elif choice == 2:
            sleep(gameSpeed)
            print("\nBugs: 'I did notice the trash bin over there was looking a little extra stuffed today! Wanna peek?'")
        elif choice == 3:
            sleep(gameSpeed)
            print("\nBugs: 'Maybe it was a ghost? Boo! Haha, just kidding!'")
        elif choice == 4 and "janitor_closet" in inventory :
            sleep(gameSpeed)
            print("\nBugs: 'Well... I guess I did close my eyes for a 10-minute magic trick! When I opened them, he was dragging some heavy black bags...'")
            if "body_moved" not in inventory:
                inventory.append("body_moved")
        elif choice == 5:
            break
        else :
            print("Bugs looks at you confused. Try another option.")

## taher
def arcade_room(inventory):
    sleep(gameSpeed)
    print(art_assets.ART_ARCADE)
    sleep(gameSpeed)
    print("Loud, flashing neon lights surround you.")
    while True:
        print("\n[1] Talk to Boyfriend")
        print("[2] Talk to Maintenance")
        print("[3] Search supply closet")
        print("[4] Leave")
        
        choice = int(input("Enter choice: "))
        if choice == 1:
            npc_boyfriend(inventory)
        elif choice == 2:
            npc_maintainence(inventory)
        elif choice == 3:
            sleep(gameSpeed)
            if "janitor_closet" in inventory:
                print("You open the closet and discover a bloody_pipe hidden inside!")
                if "bloody_pipe" not in inventory:
                    inventory.append("bloody_pipe")
            else:
                print("You don't know what you're looking for, it's just a bunch of arcade cabinets.")
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again.")

def npc_maintainence(inventory):
    sleep(gameSpeed)
    print(art_assets.ART_MAINTENANCE)
    sleep(gameSpeed)
    print("Maintenance: Hey there! How can I help?")
    while True:
        if "arcade_receipt" in inventory: # FIXED VARIABLE NAME TYPO
            print("\nQ1: What were you doing?")
            print("Q2: See anything out of the ordinary?")
            print("Q3: Any theories?")
            print("Q4: This receipt proves the Boyfriend never left. Explain this arcade token I found hidden with a bloody mop.")
            print("[5] Leave")
            choice = int(input("Select a question: "))
            if choice == 1:
                sleep(gameSpeed)
                print("\nMaintenance: Just chilling, man. Fixing the coin pushers. Jammed again. Took forever, but it's whatever.")
            elif choice == 2:
                sleep(gameSpeed)
                print("\nMaintenance: Well, the Boyfriend says he didn't move, but I saw him leave the arcade for about 15 minutes right around the time of the scream. Kinda sus, if you ask me.")
            elif choice == 3:
                sleep(gameSpeed)
                print("\nMaintenance: Honestly? Not my circus, not my monkeys. Ask the Operator. Guy sees everything from that booth.")
            elif choice == 4:
                sleep(gameSpeed)
                print("\nMaintenance: Okay, fine! I wasn't fixing machines, I was skimming tokens from the registers! I hid in the supply closet when I heard footsteps. It was the Janitor—he grabbed his mop and rushed out. I dropped a token by accident. I only lied about the Boyfriend leaving because I didn't want you looking into me!")
                if "dropped_token" not in inventory:
                    inventory.append("dropped_token")
                    print(">>> 'dropped_token' added to evidence.")
                if "janitor_closet" not in inventory:
                    inventory.append("janitor_closet")
                    print(">>> 'janitor_closet' added to evidence.")
            elif choice == 5:
                break
        else:
            print("\nQ1: What were you doing?")
            print("Q2: See anything out of the ordinary?")
            print("Q3: Any theories?")
            print("[4] Leave")
            choice = int(input("Select a question: "))
            if choice == 1:
                sleep(gameSpeed)
                print("\nMaintenance: Just chilling, man. Fixing the coin pushers. Jammed again. Took forever, but it's whatever.")
            elif choice == 2:
                sleep(gameSpeed)
                print("\nMaintenance: Well, the Boyfriend says he didn't move, but I saw him leave the arcade for about 15 minutes right around the time of the scream. Kinda sus, if you ask me.")
            elif choice == 3:
                sleep(gameSpeed)
                print("\nMaintenance: Honestly? Not my circus, not my monkeys. Ask the Operator. Guy sees everything from that booth.")
            elif choice == 4:
                break

## marwan
def npc_janitor(inventory):
    sleep(gameSpeed)
    print(art_assets.ART_JANITOR)
    while True:
        if "janitor_closet" in inventory:
            print("\nQ1: What were you doing?")
            print("Q2: See anything out of the ordinary?")
            print("Q3: Any theories?")
            print("Q4: Maintenance saw you grab your mop from the closet right at the time of the murder.")
            print("[5] Leave")
            choice = int(input("Select a question: "))
            if choice == 1:
                sleep(gameSpeed)
                print("\nJanitor: Look, captain. I was on my smoke break, standing next to that annoying rabbit. This place doesn't pay me enough to work off the clock, let alone babysit corpses.")
            elif choice == 2:
                sleep(gameSpeed)
                print("\nJanitor: Other than you bothering me? I saw her Boyfriend storming away from the coaster looking pretty mad earlier. Go bother him.")
            elif choice == 3:
                sleep(gameSpeed)
                print("\nJanitor: Yeah, my theory is lovers' quarrel. Case closed. Now if you don't mind, I got a stain to ignore.")
            elif choice == 4:
                sleep(gameSpeed)
                print("\nJanitor: Maintenance is a thief and a liar! And that stupid rabbit is blind, I was right next to him! Get out of my face before I mop the floor with you!") 
            elif choice == 5:
                break 
        else:
            print("\nQ1: What were you doing?")
            print("Q2: See anything out of the ordinary?")
            print("Q3: Any theories?")
            print("[4] Leave")
            choice = int(input("Select a question: "))
            if choice == 1:
                sleep(gameSpeed)
                print("\nJanitor: Look, captain. I was on my smoke break, standing next to that annoying rabbit. This place doesn't pay me enough to work off the clock, let alone babysit corpses.")
            elif choice == 2:
                sleep(gameSpeed)
                print("\nJanitor: Other than you bothering me? I saw her Boyfriend storming away from the coaster looking pretty mad earlier. Go bother him.")
            elif choice == 3:
                sleep(gameSpeed)
                print("\nJanitor: Yeah, my theory is lovers' quarrel. Case closed. Now if you don't mind, I got a stain to ignore.")
            elif choice == 4:
                break 

def npc_boyfriend(inventory):
    sleep(gameSpeed)
    print(art_assets.ART_BOYFRIEND)
    while True:
        if "victim_phone" in inventory:
            print("\nQ1: What were you doing?")
            print("Q2: See anything out of the ordinary?")
            print("Q3: Any theories?")
            print("Q4: I found her phone. Why didn't she call you?")
            print("[5] Leave")
            choice = int(input("Select a question: "))
            if choice == 1:
                sleep(gameSpeed)
                print("\nBoyfriend: I was playing Tekken... trying to blow off steam. We had a fight. A stupid, meaningless fight. I stayed here to cool off.")
            elif choice == 2:
                sleep(gameSpeed)
                print("\nBoyfriend: No. I was locked in, headphones on. I haven't moved from this machine in an hour. God, I know how this looks... but I loved her. I didn't do this.")
            elif choice == 3:
                sleep(gameSpeed)
                print("\nBoyfriend: It had to be someone who works here. Someone who knows the blind spots.")
            elif choice == 4:
                sleep(gameSpeed)
                print("\nBoyfriend: Because my phone died! Look! (He shows a dead phone) I swear man, if I had just swallowed my pride and gone with her...") 
                if "arcade_receipt" not in inventory:
                    inventory.append("arcade_receipt")
                    print(">>> 'arcade_receipt' added to evidence. His alibi checks out.")
            elif choice == 5:
                break 
        else:
            print("\nQ1: What were you doing?")
            print("Q2: See anything out of the ordinary?")
            print("Q3: Any theories?")
            print("[4] Leave")
            choice = int(input("Select a question: "))
            if choice == 1:
                sleep(gameSpeed)
                print("\nBoyfriend: I was playing Tekken... trying to blow off steam. We had a fight. A stupid, meaningless fight. I stayed here to cool off.")
            elif choice == 2:
                sleep(gameSpeed)
                print("\nBoyfriend: No. I was locked in, headphones on. I haven't moved from this machine in an hour. God, I know how this looks... but I loved her. I didn't do this.")
            elif choice == 3:
                sleep(gameSpeed)
                print("\nBoyfriend: It had to be someone who works here. Someone who knows the blind spots.")
            elif choice == 4:
                break 

## zaho
def coaster_room(inventory):
    sleep(gameSpeed)
    print(art_assets.ART_COASTER)
    sleep(gameSpeed)
    print("The coaster is shut down. It's dark, eerie, and the smell of grease hangs heavy in the air.")
    
    while True:
        print("\nWhat would you like to do?")
        print("[1] Talk to the Operator")
        print("[2] Search the Tracks")
        print("[3] Check the Control Panel")
        print("[4] Leave")

        choice = input("Enter choice: ")

        if choice == "1":
            npc_operator(inventory)
        elif choice == "2":
            sleep(gameSpeed)
            if "victim_phone" not in inventory:
                print("You climb onto the tracks. Near the boarding platform, you find a cracked smartphone.")
                inventory.append("victim_phone") 
                print(">>> 'victim_phone' added to evidence.")
            else:
                print("You've already searched the tracks.")
        elif choice == "3":
            sleep(gameSpeed)
            if "ride_photo" not in inventory:
                print("You check the control panel. A ride photo from the time of the murder is still on screen.")
                print("It shows a blurry figure in a staff uniform near the tracks.")
                inventory.append("ride_photo")
                print(">>> 'ride_photo' added to evidence.")
            else:
                print("The control panel screen is now dark.")
        elif choice == "4":
            break 
        else:
            print("Invalid choice.")

def npc_operator(inventory):
    sleep(gameSpeed)
    print(art_assets.ART_OPERATOR)
    while True: 
        print("\n[1] What were you doing?")
        print("[2] See anything out of the ordinary?")
        print("[3] Any theories?")
        print("[4] Leave")

        choice = input("Select a question: ")

        if choice == "1":
            sleep(gameSpeed)
            print("\nOperator: 'I-I was right here in my booth! I didn't leave, I swear! I was just doing my job pressing the buttons!'")
        elif choice == "2":
            sleep(gameSpeed)
            print("\nOperator: 'Nothing! It was dark! But... wait. Right before the screams, the janitor was up on the boarding platform.'" )
            print("'He told me he had to clean a spill! Then the screaming started!'")
            if "janitor_on_tracks" not in inventory:
                inventory.append("janitor_on_tracks")
                print(">>> Evidence added: You now know the Janitor was on the tracks.")
        elif choice == "3":
            sleep(gameSpeed)
            print("\nOperator: 'Please don't make me testify! The killer might come back for me!'")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

### start game function call ###
start_game()