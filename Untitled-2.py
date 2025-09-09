name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the Unnecessary Life Decision Maker!")

pet = input("What animal do you prefer? (Dog/Cat): ").lower()

if pet == "cat":
    activity = input("Do you scratch your cat's back, or ignore it? (scratch/ignore): ").lower()
    
    if activity == "scratch":
        print(f"{name}, the cat runs straight out the open front door!")
        
        run_action = input("Do you chase the cat or let it leave? (chase/leave): ").lower()
        if run_action == "chase":
            print(f"{name}, you sprint after the cat as it darts into the street and gets hit by a professional unicyclist.")
            
            reaction = input("Do you fight the unicyclist or call the cat ambulance? (fight/ambulance): ").lower()
            if reaction == "fight":
                print(f"{name}, you knock him out with one punch, saving your poor cat!")
            elif reaction == "ambulance":
                print(f"{name}, your cat is escorted via helicopter and you see it crash into the hillside bursting into flames.")
            else:
                print(f"{name}, confused by indecision, you just stare at the chaos.")
        else:
            print(f"{name}, you let the cat leave. It gives you a judging look as it walks away. ")
    
    elif activity == "ignore":
        print(f"{name}, the cat looks at you with judgment and decides to knock over your grandma's urn.")
        
        urn_action = input("Do you clean it up or blame the cat? (clean/blame): ").lower()
        if urn_action == "clean":
            print(f"{name}, you bend over with the broom and the ashes blow straight out your window due to a heavy wind.")
            
            reaction = input("Do you go outside to retrieve the ashes, or leave them? (retrieve/leave): ").lower()
            if reaction == "retrieve":
                print(f"{name}, you jump out the window chasing the ashes and a bird swoops down, stealing some!")
            elif reaction == "leave":
                print(f"{name}, you leave them. The wind spreads them across your neighbor's yard.")
            else:
                print(f"{name}, confused by indecision, you just stare at the ashes. ")
        
        else:
            print(f"{name}, you blame the cat. The cat looks very pleased. ")
    
    else:
        print(f"{name}, the cat is confused by your actions. ")

elif pet == "dog":
    activity = input("Do you take your dog for a walk or give it a treat? (walk/treat): ").lower()
    
    if activity == "walk":
        print(f"{name}, you leash up your dog and step outside. Suddenly, a squirrel appears riding on a goose")
        walk_action = input("Do you chase the squirrel with your dog or ignore it? (chase/ignore): ").lower()
        
        if walk_action == "chase":
            print(f"{name}, your dog drags you into a bush, spins you around like a tornado, and leaves you tangled in the leash!")
            
            stuck_action = input("Do you try to untangle yourself or call for help? (untangle/help): ").lower()
            if stuck_action == "untangle":
                print(f"{name}, you pull yourself free, only to land face-first in a giant puddle. Your dog celebrates!")
            elif stuck_action == "help":
                print(f"{name}, your neighbor arrives juggling flaming torches, while your dog happily steals their snack.")
            else:
                print(f"{name}, you freeze in panic. Your dog takes this as an invitation to start a new game.")
        
        elif walk_action == "ignore":
            print(f"{name}, your dog zooms after the squirrel, climbs the tree, and then jumps onto a trampoline left in the yard.")
            
            tree_action = input("Do you try to climb the tree or let it go? (climb/let go): ").lower()
            if tree_action == "climb":
                print(f"{name}, you climb halfway and get stuck. Meanwhile, your dog is now leading a group of stray monkeys!")
            elif tree_action == "let go":
                print(f"{name}, you decide to let the dog go. You return home and find it inside with the door locked.")
            else:
                print(f"{name}, you stare blankly. Your dog uses your head as a launching pad to chase a rogue leaf.")
        
        else:
            print(f"{name}, confused by indecision, you watch as your dog becomes the leader of the local squirrel gang.")
    
    elif activity == "treat":
        print(f"{name}, you give your dog a treat. It wags its tail so hard it creates a small windstorm, blowing your wig into the neighbor's pool!")
        
        treat_action = input("Do you chase the wig or leave it? (chase/leave): ").lower()
        if treat_action == "chase":
            print(f"{name}, you dive into the pool and emerge covered in leaves and water. Your dog barks and the neighbors come out.")
        elif treat_action == "leave":
            print(f"{name}, you leave it. Your dog immediately uses the opportunity to start eating your homework!")
        else:
            print(f"{name}, your dog looks at you skeptically, as if saying 'I taught you everything and this is what you do?'")
    
    else:
        print(f"{name}, your dog tilts its head in confusion, judging your life choices.")

else:
    print(f"{name}, interesting choice, but we only handle cats or dogs here!")






    
  
