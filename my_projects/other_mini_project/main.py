#!/usr/bin/python3

"""Main file for week 2 mini project (start)"""
# print opening story and instructions
def showinstructions():
    print("Mountain of Madness\n")
    print("")
    print("You awaken from a strange dream and find yourself on the beach of a strange mountain ")
    print("in the middle of the ocean. The remains of a shattered boat lay cast around you. ")
    print("You're not sure how you got here, and don't remember even getting on a boat. The one ")
    print("thing you do know is a storm is moving in and the tide seems to rising quickly. You ")
    print("spot a cave to the north that should provide you some shelter from the weather. \n")
    print("Move Commands: go 'north', 'south', 'east', 'west'")
    print("Add to Inventory: get 'Item'")
    print("-----------------------------------------------------------------------")


def showstatus():
    """determine the current status of the player"""
# print the player's current location
    print('---------------------------')
    print('You are in the ' + current_room)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if 'item' in rooms[current_room]:
        print('You see a ' + rooms[current_room]['item'])
    if 'monster' in rooms[current_room]:
        print('You feel a presence')   
    print("---------------------------")

    # Create a dictionary to house the rooms and items
inventory = []

rooms = {
        'Boat wreckage': {'name': 'Boat wreckage',
            'north': 'Cave entrance', 
            'item': 'flashlight'
                },
        'Cave entrance': {'name': 'Cave entrance',
            'north': 'Corridor', 
            'east': 'Pit', 
            'south': 'Boat wreckage',
            'item': 'rope'
                },
        'Pit': {'name': 'Pit',
            'west': 'Cave entrance', 
            
                },
        'Corridor': {'name': 'Corridor',
            'south': 'Cave entrance', 
            'north': 'Chamber',
            'item': 'carved idol'
                },
        'Chamber': {'name': 'Chamber',
            'west': 'Stream', 
            'east': 'Tunnel',
            
                },
        'Tunnel': {'name': 'Tunnel',
            'west': 'Chamber',
            'item': 'strange knife'
                },
        'Stream': {'name': 'Stream',
            'south': 'Underground lake', 
            'east': 'Chamber',
            
            'monster': 'creature'
                },
        'Underground lake': {'name': 'Underground Lake',
            'north': 'Stream',
            
            'monster': 'darkness'
                },
            }
    # Establish how players current location will be called
current_room = 'Boat wreckage'

showinstructions()

# breaking this while loop means the game is over
while True:
    showstatus()
    move = ''
    while move == '':  
        move = input('>')
    # normalizing input:         
    move = move.lower().split(" ", 1)

        #if they type 'go' first
    if move[0] == 'go':
            #check that they are allowed wherever they want to go
        if move[1] in rooms[current_room]:
                #set the current room to the new room
            current_room = rooms[current_room][move[1]]
            # if they aren't allowed to go that way:               
        else:
            print('The madness of this place must be getting to you. Please give a valid command.')
    if move[0] == 'get' :
            
        if "item" in rooms[current_room] and move[1] in rooms[current_room]['item']:
                #add the item to their inventory
            inventory.append(move[1])
                #display a helpful message
            print(move[1] + ' got!')
                #delete the item key:value pair from the room's dictionary
            del rooms[current_room]['item']
            # if there's no item in the room or the item doesn't match
        else:
                #tell them they can't get i
            print('The madness of this place must be getting to you. Please give a valid command.')

        ## Define the rooms
    if current_room == 'Cave entrance':
        print('You enter the cave and notice some odd markings along the wall, and some old rope coiled in the corner.')
        print('There is an opening in the rock leading to the east and a long corridor to the north. ')
    if current_room == 'Pit':
        print('You squeeze through the opening in the wall. It opens up just as the floor falls away before your feet.')
        print('You manage to stumble back and avoid falling into the abyss.')
        if 'rope' in inventory:
            print('Across the pit you notice a strange looking knife stuck between two rocks. You attempt to secure it with rope, but miss and you can only watch')
            print('as the knife falls disappearing into the darkness') 
    if current_room == 'Corridor':
        print('You continue deeper into the cave. The path seems to be leading deeper into Earth, yet the ocean which was only feet away from the entrance')
        print("is nowhere to be found. The deeper you go the higher in altitude you feel. Are you losing your senses or your mind? The thought is interupted")
        print('as you come to an opening to what you believe is the north. You see a small stone that appears to be glowing in the darkness. On closer')
        print("inspection, you see that it is a carving of a humanoid figure. It's almost as if the small idol is guarding the path")
    if current_room == 'Chamber' :
        print("The corridor opens into a vast chamber. You can no longer see the ceiling above your head, although honestly you're not certain")
        print('which way is actually up anymore. There is what looks to be a fountain carved from the stone floor feeding a stream that flows west across ')
        print('the chamber. The water seems to rise from the fountain, but you only see a solid stone base. Carved into the polished stone of the fountain')
        print("are images you've never seen and are somehow beyond the description of any human language")
        if 'rope' in inventory:
            print('As you stand there mesmorized by the images that seem to be moving in the stone you catch a shimmer in the corner of your eye.')
            print('Off to the east is a small tunnel and there is something shining from within')
    if current_room == 'Tunnel':
        print('You crawl your way into the tunnel following the shimmer in the distance. As you reach it you realize it is the strange knife from earlier.')
        print('The knife is resting on a pile bones. Some you recognize as human, others seem too large and misshapen. This must be the bottom of the pit')
    if current_room == 'Stream':
        print("You follow the stream for a while when you start to get the feeling you're being watched. You turn around to see a figure standing just a few meters behind you.")
        if 'carved idol' in inventory:
            print('as the figure moves closer you notice the glow from the idol in your pocket becomes brighter. The figure stops in his tracks and bows down, slowly backing away')
            print("into the darkness. You hurry further along the path as it curves to the south. You aren't sure what happened but aren't sure you want to know either.")
        elif 'Strange knife' in inventory:
            print("You attempt to pull out the knife you found, but there is no time. The figure seems to multiply before your eyes as it engulfs you. You're drug")
            print('to the fountain and submerged into the vast pool of water. The water feels like a living thing surrounding you and setting every nerve')
            print(' ending aflame. The pain is agonizing and you cam mo longer hold your breath. You finally give in hoping for the release of death and inhale sharply')
            print('only to realize you can still breath in this living liquid. What is this and how long must you endure it? It looks like you will have plenty of time to contemplate')
            break
        else:
            print("You want to run but as you turn back there is another one. The figures seem to multiply before your eyes as they engulf you. You're drug")
            print('to the fountain and submerged into the vast pool of water. The water feels like a living thing surrounding you and setting every nerve')
            print('ending aflame. The pain is agonizing and you cam mo longer hold your breath. You finally give in hoping for the release of death and inhale sharply')
            print('only to realize you can still breath in this living liquid. What is this and how long must you endure it? It looks like you will have plenty of time to contemplate')
            break
            
    if current_room == 'Underground lake':
        print('You continue following the stream until it reaches a fall and pours into a vast underground lake. The lake appears to respond to your presense and begins churning.')
        print('You catch a glimps of something in the water and lean over to get a better look.')
        if 'strange knife' in inventory:
            print('Before you can react you are pulled into the lake by an unseen force. You swim towards the closest bank, but the water begins to cloud black')
            print('like a dozen octopi scatterd in trails of ink at once. You find yourself struggling more to swim as the cloud rises around you. It feels as if')
            print('the water itself is trying to drag you down. The harder you swim the further the shore drifts away. In an act of pure desperation you pull the')
            print('strange knife out and begin swinging it wildly in every direction. As you continue to flail in fear you notice the waters grasp on you loosen.')
            print('Unsure of what is happening, or if any of it is correlated, you sieze the opening and head for dry ground. Slicing a path in front of you')
            print('as you scramble towards the landing you can feel the darkness fleeing from the blade. You reach the bank of the lake and collapse from exaustion.')
            print('As you fade out of conscienceness you think you see a form beneath waters surface looking back at you. \n')
            print("The next time you open your eyes you're laying drenched in sweat in your own bed. You tell yourself it was just a dream, but as you sit up")
            print("you feel something in your pocket. You reach in to grab it and feel the shape of the carved idol, hot to the touch...")
            break
        else:
            print('Before you can react you are pulled into the lake by an unseen force. You swim towards the closest bank, but the water begins to cloud black')
            print('like a dozen octopi scatterd in trails of ink at once. You find yourself struggling more to swim until you finally become immobile.')
            print("The water around you becomes heavier, applying pressure from every direction. It's as if the darkness itself is constricting you")
            print('with each breath the pressure builds until you can no longer expand your lungs. Just as the blackness enveloped the water, so it begins to')
            print('swallow your vision. The last thing you see before flling unconscious is...')
            break


#if __name__ == "__main__":
#    main()
