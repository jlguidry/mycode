def showstatus(current_room, inventory, rooms):
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



