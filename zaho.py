# Zaho's part
def coaster_room(inventory):
    print("\n--- Roller Coaster---")
    print("The coaster is shut down. It's dark, eerie, and the smell of grease hangs heavy in the air.")
    
    while True: #to start a room loop
        print("\nWhat would you like to do?")
        print("[1] Talk to the Operator")
        print("[2] Search the Tracks")
        print("[3] Check the Control Panel")
        print("[4] Leave")

        choice= input("Enter choice: " )

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
                






