import art_assets

inventory = []

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
            
