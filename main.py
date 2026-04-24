from time import sleep
import art_assets

# player variables
inventory = []
name = ""

# game state variables
game_running = False

## karim
def start_game():
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
                yOrn = input("[yes] [no]\n")
                if (yOrn.lower() == "yes") or (yOrn.lower() == "y"):
                    make_accusation(inventory)
                elif (yOrn.lower() == "no") or (yOrn.lower() == "n"):
                    print(f"Good choice, {name}. You should gather more evidence before making an accusation.")
            else:
                make_accusation(inventory)

def make_accusation(inventory):
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
    global name
    start_screen = True

    print("================== Murder Mystery ==================")
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
    pass

def npc_bugs(inventory):
    pass

## taher
def arcade_room(inventory):
    pass

def npc_maintenance(inventory):
    pass

## marwan
def npc_janitor(inventory):
    pass

def npc_boyfriend(inventory):
    pass

## zaho
def coaster_room(inventory):
    pass

def npc_operator(inventory):
    pass

### start game function call ###
start_game()

