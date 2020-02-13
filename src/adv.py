from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['stick']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['wine', 'bat', 'wrench']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['gun', 'c4', 'map']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['note', 'skull']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('dude', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
selection = ''

def itemtoRoom(items):
    print(items, 57)
    itemsMatchingInventoryList = list(filter(lambda item: item in newPlayer.inventory, items))
    if len(itemsMatchingInventoryList) > 0:
        for item in itemsMatchingInventoryList:
            newPlayer.inventory.remove(item)
            newPlayer.room.listItems.append(item)
            print(f'successfully dropped {item}')
    else:
        print(f"item doesn't exist in {newPlayer.room.name} at the moment")

def itemtoInventory(items):
    itemsMatchingRoomList = list(filter(lambda item: item in newPlayer.room.listItems, items))
    if len(itemsMatchingRoomList) > 0:
        for item in itemsMatchingRoomList:
            newPlayer.inventory.append(item)
            newPlayer.room.listItems.remove(item)
            print(f'successfully picked {item}')
    else:
        print(f"item(s) doesn't exist in {newPlayer.room.name} at the moment")
    
def actions(itemObject):
    if 'pick' in selection:
        itemtoInventory(itemObject)
    elif 'drop' in selection:
        itemtoRoom(itemObject)

while selection != 'q':
    print(F"{newPlayer.player_name} is in {newPlayer.room.name}; items available: {list(newPlayer.room.listItems)}")
    #items = map(lambda n: print(n), newPlayer.room.listItems)
    #print(f'Items available in room: {list(newPlayer.room.listItems)}')
    selection = str(input('Select cardinal point to move in direction:\n    -  [n] North  [e] East  [s] South  [w] West\n'
         'Type in action to drop or pick item:\n    -  pick {item}  drop {item}\n'
    )).lower()
    itemObject = selection.split()[1:]
    try:
        if selection == "i":
            print(f'Inventory: {list(newPlayer.inventory)}')
        elif 'Outside' in newPlayer.room.name:
            actions(itemObject)
            if selection == "n":
                newPlayer.room = room["foyer"]
            elif (selection == "e") or (selection =="s") or (selection =="w"):
                print('Error, you cannot go that way')
        elif 'Foyer' in newPlayer.room.name:
            actions(itemObject)
            if selection == "n":
                newPlayer.room = room["overlook"]
            elif selection == "s":
                newPlayer.room = room["outside"]
            elif selection == "e":
                newPlayer.room = room["narrow"]
            elif (selection =="w"):
                print('Error, you cannot go that way')
        elif 'Narrow' in newPlayer.room.name:
            actions(itemObject)
            if selection == "n":
                newPlayer.room = room["treasure"]
            elif selection == "w":
                newPlayer.room = room["foyer"]
            elif (selection == "e") or (selection =="s"):
                print('Error, you cannot go that way')
        elif 'Treasure' in newPlayer.room.name:
            actions(itemObject)
            if selection == "s":
                newPlayer.room = room["narrow"]
            elif (selection == "n") or (selection =="e") or (selection =="w"):
                print('Error, you cannot go that way')
        elif 'Overlook' in newPlayer.room.name:
            actions(itemObject)
            if selection == "s":
                newPlayer.room = room["foyer"]
            elif (selection == "n") or (selection =="e") or (selection =="w"):
                print('Error, you cannot go that way')
    except:
        print('Kindly pick a valid input')