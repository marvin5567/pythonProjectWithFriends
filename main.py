from time import sleep # this is used to create a delay between prints, to make the game feel more immersive and less rushed
import art_assets # this is where all the ascii art will be stored, and we can import it here to use it in our main game file

# player variables
inventory = []
name = ""

# game state variables
game_running = False

## karim
def start_game():
    # this function will contain the main game loop, and will be responsible for calling the intro sequence as well
    # as any choices/functions the player will need to call
    game_running = True
    intro()
    while game_running:            
        choice = int(input(f"{name} (in your head): Alright, what should I do?\nGo To:\n[1] Roller Coaster \n[2] Arcade \n[3] Canteen \n\nActions:\n[4] View Evidence\n[5] Accuse\n"))
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
                    make_accusation(inventory)
                elif (yesOrno.lower() == "no") or (yesOrno.lower() == "n"):
                    print(f"Good choice, {name}. You should gather more evidence before making an accusation.")
            else:
                make_accusation(inventory)

def make_accusation(inventory):
    # function yet to be made
    print("You have presented your evidence.")

def view_evidence(inventory):
    print(art_assets.ART_EVIDENCE)
    if len(inventory) == 0:
        print("You have no evidence in your inventory.")
    else:
        print("You have the following evidence in your inventory:")
        for item in inventory:
            print(f"- {item}")
    print("====================")


def intro():
    # this function will be responsible for the intro sequence, and also take care of a few things
    # such as setting the player's name
    global name # we need to declare this as global so that we can modify it inside the function, and have the changes reflected outside the function as well
    start_screen = True

    print("================== Murder Mystery ==================")
    print(art_assets.ART_TITLE)
    print("################# Carnival Canaver #################")
    while start_screen:
        sleep(0.5)
        choice = int(input("[1] Play\n[2] Settings\n[3] Quit\n"))
        if choice == 1:
            start_screen = False
        if choice == 2:
            print("Settings menu would be displayed here. work on this later marvin")
        if choice == 3:
            print("Thanks for playing!")
            SystemExit()
    name = input("What is your name, detective? ")
    print(art_assets.ART_COP)
    sleep(1.5)
    print(f"Officer: Welcome, detective {name}! Let me fill you in on the details.")
    sleep(1.5)
    print("Officer: The victim was a woman, aged 22, found dead in trash bags in the canteen")
    sleep(1.5)
    print("Officer: In addition, witness reports and forensic data suggets that the murder took place in the roller coaster.")
    sleep(1.5)
    print("Officer: On the carnival site, we have five suspects, scattered in 3 different areas. Do well detective, and catch that souless bastard!")
    sleep(1.5)
    print(f"{name}: You can count on me officer :)")
    sleep(1.5)

## okasha
def canteen_room(inventory):
    while True:
        print("=== THE CANTEEN ===")
        print("A messy, brightly lit area. There are Bugs Bunny and The Janitor.")
        print("1: Talk to Bugs Bunny")
        print("2: Talk to The Janitor")
        print("3: Inspect the Trash Bin")
        print("4: Leave the Canteen")

        choice = int(input("what u want to do??"))
        if choice == 1 :
            npc_bugs(inventory)
        elif choice == 2 :
            npc_janitor(inventory)
        elif choice == 3 :
            if "bloody_gloves" not in inventory :
                print("You dig through the bin and find a pair of bloody_gloves!")
                inventory.append("bloody_gloves")
            else :
                print("The bin is empty now.")
        elif choice == 4 :
            break
        else:
            print("try another choice.")     

def npc_bugs(inventory):
    while True :
        print("--- Bugs Bunny ---")
        print("Q1:What were you doing??")
        print("Q2:Did you See anything out of the ordinary?")
        print("Q3:Have any theories?")
        if "janitor_closet" in inventory:
            print("Q4:Are you sure the Janitor was with you the whole time?")
        print("5:leave")

        choice = int(input("Select a question to ask Bunny or leave(5): "))
        if choice == 1:
            print("\nBugs: 'Oh, howdy pal! I was just entertaining the kiddos over by the prize booth! My buddy the Janitor was right next to me!'")
        elif choice == 2:
            print("\nBugs: 'I did notice the trash bin over there was looking a little extra stuffed today! Wanna peek?'")
        elif choice == 3:
            print("\nBugs: 'Maybe it was a ghost? Boo! Haha, just kidding!'")
        elif choice == 4 and "janitor_closet" in inventory :
            print("\nBugs: 'Well... I guess I did close my eyes for a 10-minute magic trick! When I opened them, he was dragging some heavy black bags...'")
            if "body_moved" not in inventory:
                inventory.append("body_moved")
        elif choice == 5:
            break
        else :
            print("Bugs looks at you confused. Try another option.")

## taher
def arcade_room(inventory):
    print(art_assets.ART_ARCADE)
    while True:
        choice= int(input("1. Talk to Boyfriend \n 2. Talk to Maintainence \n 3. Search supply closet \n 4. Leave" ))
        if choice== 1:
            npc_boyfriend(inventory)
        if choice== 2:
            npc_maintainence(inventory)
        if choice== 3:
            if "janitor_closet" in inventory:
                inventory.append("bloody_pipe")
            else:
                print("You dont know what you're looking for, its just a bunch of arcade cabinets")
        if choice==4:
            break
        else:
            print("Invalid choice, please try again")

def npc_maintainence(inventory):
    while True:
        if" arcade_reciept" in inventory:
            choice = int(input("Q1: What were you doing? \n Q2: See anything out of the ordinary? \n Q3: Any theories? \n Q4: This receipt proves the Boyfriend never left. Explain this arcade token I found hidden with a bloody mop. \n 5. Leave"))
            if choice== 1:
                print("Just chilling, man. Fixing the coin pushers. Jammed again. Took forever, but it's whatever.")
            if choice==2:
                print("Well, the Boyfriend says he didn't move, but I saw him leave the arcade for about 15 minutes right around the time of the scream. Kinda sus, if you ask me.")
            if choice==3:
                print("Honestly? Not my circus, not my monkeys. Ask the Operator. Guy sees everything from that booth.")
            if choice==4:
                print("Okay, fine! I wasn't fixing machines, I was skimming tokens from the registers! I hid in the supply closet when I heard footsteps. It was the Janitor—he grabbed his mop and rushed out. I dropped a token by accident. I only lied about the Boyfriend leaving because I didn't want you looking into me!")
                inventory.append("dropped_token")
                inventory.append("janitor_closet")
            if choice==5:
                break
        else:
            choice = int(input("Q1: What were you doing? \n Q2: See anything out of the ordinary? \n Q3: Any theories?\n4.Leave"))
            if choice== 1:
                print("Just chilling, man. Fixing the coin pushers. Jammed again. Took forever, but it's whatever.")
            if choice==2:
                print("Well, the Boyfriend says he didn't move, but I saw him leave the arcade for about 15 minutes right around the time of the scream. Kinda sus, if you ask me.")
            if choice==3:
                print("Honestly? Not my circus, not my monkeys. Ask the Operator. Guy sees everything from that booth.")
            if choice==4:
                break

## marwan
def npc_janitor(inventory):
    pass

def npc_boyfriend(inventory):
    pass

## zaho
def coaster_room(inventory):
    print("\n--- Roller Coaster---")
    print("The coaster is shut down. It's dark, eerie, and the smell of grease hangs heavy in the air.")
    
    while True: #to start a room loop
        print("\nWhat would you like to do?")
        print("[1] Talk to the Operator")
        print("[2] Search the Tracks")
        print("[3] Check the Control Panel")
        print("[4] Leave")

        choice = input("Enter choice: " )

        if choice == "1":
            npc_operator(inventory)
        elif choice =="2":
            if "victim_phone" not in inventory:
                print("\nYou climb onto the tracks. Near the boarding platform, you find a cracked smartphone.")
                inventory.append("victim_phone") #which means we have found the phone
                print(">>> 'victim_phone' added to inventory.")
            else:
             print("\nYou've already searched the tracks.")
        elif choice == "3":
            if "ride_photo" not in inventory:
                print("\nYou check the control panel. A ride photo from the time of the murder is still on screen.")
                print("It shows a blurry figure in a staff uniform near the tracks.")
                inventory.append("ride_photo")
                print(">>> 'ride_photo' added to inventory.")
            else:
                print("\nThe control panel screen is now dark.")
        elif choice == "4":
            break # to stop the room loop
        else:
            print(" Invalid choice.")

def npc_operator(inventory):
    
    while True: # to start the NPC loop
        print("\n--- The Operator ---")
        print("[1] What were you doing?")
        print("[2] See anything out of the oridnary?")
        print("[3] Any theories?")
        print("[4] Leave")

        choice= input("Enter choice: ")

        if choice == "1":
            print("\nOperator: 'I-I was right here in my booth! I didn't leave, I swear! I was just doing my job pressing the buttons!")
        elif choice =="2":
            print("\nOperator: 'Nothing! It was dark! But... wait. Right before the screams, the janitor was up on the boarding platform.'" )
            print("'He told me he had to clean a spill! Then the screaming started!'")
            if "janitor_on_tracks" not in inventory:
                inventory.append("janitor_on_tracks") #clue
                print(">>> Clue added: You now know the Janitor was on the tracks.")
            elif choice =="3":
                print("\nOperator: 'Please don't make me testify! The killer might come back for me!'")
            elif choice == "4":
                break
            else:
                print("Invalid choice.")

### start game function call ###
start_game()

