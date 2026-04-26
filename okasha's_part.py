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
