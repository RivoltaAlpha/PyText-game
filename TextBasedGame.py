# Full Name: [Your Name]

def print_dungeon_map():
    # This function prints the dungeon map.
    map_string = """
                   [Landing Site]-- [Forest]
                       |                |
                       v                V
                   [Desert]       [Alien Fortress]
    """
    print(map_string)


def show_instructions():
    """
    This function displays the instructions of the game.
    It shows the goal, movement commands, and how to collect items.
    """
    print("Text Adventure Game")
    print("The player must collect all the items to survive and defeat the Alien Overlord.")
    print("Goal: Collect all 3 items from different rooms to win, but avoid the villain!")
    print("Moving commands: go North, go South, go East, go West")
    print("To add an item to your Inventory type: get 'item name'")
    print("This is the Map:")
    print_dungeon_map()


def show_status(current_room, inventory, rooms):
    """
    This function displays the player's current status.
    It shows the player's current room, inventory, and available item in the room which they can collect.

    Parameters used:
        current_room (str): The player's current location.
        inventory (list): The player's list of collected items.
        rooms (dict): The dictionary linking rooms to other rooms and items.
    """
    print(f"You are in the {current_room}")
    print(f"Collected Items: {inventory}")
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print()


def move_to_new_room(current_room, player_input, rooms):
    """
    This function updates the player's current room based on their input.
    """
    if player_input in rooms[current_room]:
        return rooms[current_room][player_input]
    else:
        print("Invalid direction! Try again.")
        return current_room


def main():
    """
    The main function that controls the gameplay.
    It initializes the game, handles user input, and determines win/lose conditions.
    """

    # Dictionary mapping rooms to other rooms and items
    rooms = {
        'Landing Site': {'South': 'Desert', 'East': 'Forest', 'item': 'Map'},
        'Desert': {'North': 'Landing Site', 'item': 'Water Bottle'},
        'Forest': {'West': 'Landing Site', 'South': 'Alien Fortress', 'item': 'Shield'},
        'Alien Fortress': {'North': 'Forest', 'item': 'Alien Overlord'},  # Villain room
    }

    # Player starts in the 'Landing Site' with an empty inventory
    current_room = 'Landing Site'
    inventory = []
    player_has_won = False
    player_is_alive = True
    total_items_to_collect = 3

    # Show the game instructions
    show_instructions()

    # Start the game loop
    while not player_has_won and player_is_alive:
        # Display the player's current status and available commands
        show_status(current_room, inventory, rooms)

        # Prompt player for their move (either move or collect an item)
        player_input = input("Enter your move: ").strip().title().split(" ")

        # Handle movement (e.g., 'go North')
        if player_input[0] == 'Go' and len(player_input) > 1:
            new_room = move_to_new_room(current_room, player_input[1], rooms)
            if new_room != current_room:
                current_room = new_room
            print(f"You've moved to {current_room}.")

        # Handle item collection (e.g., 'get Map')
        elif player_input[0] == 'Get' and len(player_input) > 1:
            if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == " ".join(
                    player_input[1:]).lower():
                item = rooms[current_room]['item']
                if item != 'Alien Overlord':  # Prevent player from "getting" the villain
                    inventory.append(item)
                    print(f"{item} collected!")
                    del rooms[current_room]['item']  # Remove the item from the room
                else:
                    # Player encounters the villain and loses the game
                    print("You've encountered the Alien Overlord! GAME OVER!")
                    player_is_alive = False
            else:
                print("No such item here! Please try again.")

        else:
            print("Invalid command! Please use 'go [direction]' or 'get [item]'.")

        # Check if the player has collected all items and won the game
        if len(inventory) == total_items_to_collect:
            print("Congratulations! You've collected all items and escaped!")
            player_has_won = True
            player_is_alive = True

        # Check if the player has entered the Alien Fortress and lost the game
        if current_room == 'Alien Fortress' and not player_has_won:
            print("You've encountered the Alien Overlord! GAME OVER!")
            player_is_alive = False

    # End game messages
    if player_has_won:
        print("Congratulations! You've collected all artifacts and restored peace!")
    if not player_is_alive:
        print("Thanks for playing the game. Hope you enjoyed it.")


# Main function to start the game
if __name__ == "__main__":
    main()
