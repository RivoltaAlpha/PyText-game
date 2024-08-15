# TextBasedGame.py
# Full Name: [Your Name]

def print_dungeon_map():
    # This function prints the dungeon map.
    map_string = """
                   [Dungeon]         
                       |                
                       v                
     [Library]  -- [Great Hall] -- [Kitchen]
                       |                |
                       v                V
                   [Bedroom]         [Dining Room]
                        \\       
                          V          
                      [Cellar ]
    """
    print(map_string)


def show_instructions():
    """
    This function displays the instructions of the game.
    It shows the goal, movement commands, and how to collect items.
    """
    print("Text Adventure Game")
    print("Goal: Collect all 6 items in different rooms so as to win, but avoid the villain! The Dragon.")
    print("Moving commands: go North, go South, go East, go West")
    print("To add an item to your Inventory type: get 'item name'")
    print('Guess the wrong room and you''re dead. Good luck!')
    print("This is the Dungeon Map:")
    print_dungeon_map()


def show_status(current_room, inventory, rooms):
    """
    This function displays the player's current status.
    It shows the player's current room, inventory, and available item in the room.

    Parameters:
        current_room (str): The player's current location.
        inventory (list): The player's list of collected items.
        rooms (dict): The dictionary linking rooms to other rooms and items.
    """
    print(f"You are in the {current_room}")
    print(f"Collected Items: {inventory}")
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print()


def main():
    """
    The main function that controls the gameplay.
    It initializes the game, handles user input, and determines win/lose conditions.
    """

    # Dictionary mapping rooms to other rooms and items (if any)
    rooms = {
        'Great Hall': {'South': 'Bedroom', 'North': 'Dungeon', 'East': 'Kitchen', 'West': 'Library'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar', 'item': 'Armor'},
        'Cellar': {'West': 'Bedroom', 'item': 'Helmet'},
        'Kitchen': {'West': 'Great Hall', 'South': 'Dining Room', 'item': 'Sword'},
        'Library': {'East': 'Great Hall', 'item': 'Shield'},
        'Dungeon': {'South': 'Great Hall', 'item': 'Magic Potion'},
        'Dining Room': {'North': 'Kitchen', 'item': 'Dragon'}  # Villain room
    }

    # Player starts in the 'Great Hall' with an empty inventory
    current_room = 'Great Hall'
    inventory = []
    total_items_to_collect = 6
    items_to_collect = {'Armor', 'Helmet', 'Sword', 'Shield', 'Magic Potion', 'Dragon'}  # List of all items to win

    # Show the game instructions
    show_instructions()

    while True:
        # Display the player's current status and available commands
        show_status(current_room, inventory, rooms)

        # Prompt player for their move (either move or collect an item)
        move = input("Enter your move: ").strip().title()

        # Splitting the move into action and potential item name/direction
        action = move.split(" ", 1)
        command = action[0]
        argument = action[1] if len(action) > 1 else None

        # Handling movement (e.g., 'go North')
        if command == 'Go':
            if argument in rooms[current_room]:
                current_room = rooms[current_room][argument]
            else:
                print("Invalid direction! Please try again.")

        # Handling item collection (e.g., 'get Sword')
        elif command == 'Get':
            if argument and 'item' in rooms[current_room]:
                item_name = rooms[current_room]['item']
                if item_name.lower() == argument.lower():
                    if item_name != 'Dragon':
                        if item_name not in inventory:
                            inventory.append(item_name)
                            print(f"{item_name} collected!")

                            # Remove the item from the room
                            del rooms[current_room]['item']
                        else:
                            print("You already have this item.")
                    else:
                        # Player loses the game if they encounter the Dragon
                        print("NOM NOM... The dragon got you! GAME OVER!")
                        print("Thanks for playing the game. Hope you enjoyed it.")
                        return  # Exits the game
                else:
                    print("No such item here! Please try again.")
            else:
                print("No such item here! Please try again.")

        # Handle invalid input commands
        else:
            print("Invalid command! Please use 'go [direction]' or 'get [item]'.")

        # Check win condition (if the player has collected all items)
        if len(inventory) == total_items_to_collect:
            print("Congratulations! You have collected all items and defeated the game!")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break


# Run the main function to start the game
# if __name__ == "__main__":
    main()
