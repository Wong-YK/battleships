#see the readme.md file for description and data
import random
import copy

def is_sunk(ship):
    """
    returns Boolean value, which is True if ship is sunk and False otherwise
    """
    return ship[3]==len(ship[4])

def ship_type(ship):
    """
    returns one of the strings "battleship", "cruiser", "destroyer", or "submarine"
    identifying the type of ship
    """
    if ship[3]==4:
        return "battleship"
    elif ship[3]==3:
        return "cruiser"
    elif ship[3]==2:
        return "destroyer"
    else:
        return "submarine"

def is_open_sea(row, column, fleet):
    """
    checks if the square given by row and column neither contains nor is adjacent
    (horizontally, vertically, or diagonally) to some ship in fleet. Returns Boolean
    True if so and False otherwise
    """
    occupied_adjacent=set()
    for ship in fleet:
        for i in range(-1, ship[3] + 1):
            if ship[2]:
                #compiles occupied and adjacent squares for horizontal ships
                occupied_adjacent|={(ship[0], (ship[1]+i)), ((ship[0]-1), (ship[1]+i)), ((ship[0]+1), (ship[1]+i))}
            else:
                #compiles occupied and adjacent squares for vertical ships
                occupied_adjacent|={((ship[0]+i), ship[1]), ((ship[0]+i), (ship[1]-1)), ((ship[0]+i), (ship[1]+1))}
    if (row, column) in occupied_adjacent: return False
    else: return True

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """
    checks if addition of a ship, specified by row, column, horizontal, and
    length, to the fleet results in a legal arrangement. If so, the function
    returns Boolean True and it returns False otherwise. This function makes
    use of the function is_open_sea
    """
    #compile coordinates that the ship occupies
    ship_coords = set()
    for i in range(length):
        if horizontal:
            ship_coords|={(row, column+i)}
        else:
            ship_coords|={(row+i, column)}
    #check that each coordinate the ship occupies is within the confines of the
    #board and is in open sea
    ok = True
    for coord in ship_coords:
        if (coord[0]<0 or coord[0]>9 or coord[1]<0 or coord[1]>9
            or not is_open_sea(coord[0], coord[1], fleet)): ok = False
        else: continue
    return ok

def place_ship_at(row, column, horizontal, length, fleet):
    """
    returns a new fleet that is the result of adding a ship, specified by row, column,
    horizontal, and length as in ship representation above, to fleet. It may be assumed
    that the resulting arrangement of the new fleet is legal
    """
    fleet.append((row, column, horizontal, length, set()))
    return fleet

def randomly_place_all_ships():
    """
    returns a fleet that is a result of a random legal arrangement of the 10 ships in the
    ocean. This function makes use of the functions ok_to_place_ship_at and place_ship_at
    """
    fleet = []
    lengths = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for length in lengths:
        #find a random legal placement
        placement_legal = False
        while not placement_legal:
            row = random.randrange(0, 10)
            col = random.randrange(0, 10)
            horizontal = random.choice([True, False])
            placement_legal = ok_to_place_ship_at(row, col, horizontal, length, fleet)
        #add legally placed ship to fleet
        fleet = place_ship_at(row, col, horizontal, length, fleet)
    return fleet

def check_if_hits(row, column, fleet):
    """
    returns Boolean value, which is True if the shot of the human player at the square
    represented by row and column hits any of the ships of fleet, and False otherwise
    """
    #compile coordinates occupied by all ships in fleet
    ship_coords = set()
    for ship in fleet:
        for i in range(ship[3]):
            if ship[2]:
                ship_coords |= {(ship[0], ship[1] + i)}
            else:
                ship_coords |= {(ship[0] + i, ship[1])}
    #check if any of the coordinates occupied by a ship matches those of the shot
    hit = False
    for coord in ship_coords:
        if (row, column)==coord:
            hit = True
            break
        else: continue
    return hit

def hit(row, column, fleet):
    """
    returns a tuple (fleet1, ship) where ship is the ship from the fleet that receives
    a hit by the shot at the square represented by row and column, and fleet1 is the
    fleet resulting from this hit. It may be assumed that shooting at the square row,
    column results in hitting of some ship in fleet
    """
    for ship in fleet:
        #determine the coordinates of a particular ship
        ship_coords = set()
        for i in range(ship[3]):
            if ship[2]:
                ship_coords |= {(ship[0], ship[1] + i)}
            else:
                ship_coords |= {(ship[0] + i, ship[1])}
        #determine if the hit coordinates match any of the ship's coordinates
        if (row, column) in ship_coords:
            ship[4].add((row, column))
            return (fleet, ship)
        else: continue

def are_unsunk_ships_left(fleet):
    """
    returns Boolean value, which is True if there are ships in the fleet that are still
    not sunk, and False otherwise
    """
    for ship in fleet:
        if not is_sunk(ship):
            return True
        else: continue
    return False

def is_valid_input(input_list):
    """
    takes a list, generated from player input specifying coordinates of a shot, and
    returns True if the list contains exactly two integers which are both less than 10 and
    greater than or equal to 0 and false otherwise
    """
    input_list_copy = copy.deepcopy(input_list)
    try:
        for i in range(len(input_list_copy)):
            input_list_copy[i]=int(input_list_copy[i])
        if (len(input_list_copy)!=2
            or input_list_copy[0] < 0 or input_list_copy[0] > 9
            or input_list_copy[1] < 0 or input_list_copy[1] > 9):
                input_valid = False
        else:
            input_valid = True
    except:
        input_valid = False
    return input_valid

def coords_already_targeted(row, column, shots_fired):
    """
    takes two integers specifying the row and column of the square that the player is
    currently targeting in addition to a set which contains a record of squares that have
    been previously shot at; returns True if the square currently being targeted has
    previously been shot at and False if otherwise
    """
    if (row, column) in shots_fired:
        already_targeted = True
    else:
        already_targeted = False
    return already_targeted

def main():
    """
    returns nothing. It prompts the user to call out rows and columns of shots and
    outputs the responses of the computer iteratively until the game stops. Further
    requirements: (a) there must be an option for the human player to quit the game
    at any time, (b) the program must never crash (i.e., no termination with Python
    error messages), whatever the human player does.
    """
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = []

    while not game_over:
        loc_str = input("Enter row and column to shoot (separted by space) or enter q to quit: ").split()
        #quit game if player inputs "q"
        if loc_str==["q"]: break
        #if input is not valid prompt player for valid input
        elif not is_valid_input(loc_str):
            print("Invalid input, please try again")
            continue
        else:
            current_row = int(loc_str[0])
            current_column = int(loc_str[1])
            if (not check_if_hits(current_row, current_column, current_fleet)
                or coords_already_targeted(current_row, current_column, shots)):
                print("You missed!")
            else:
                print("You have a hit!")
                (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                if is_sunk(ship_hit):
                    print("You sank a " + ship_type(ship_hit) + "!")
            shots.append((current_row, current_column))

        if not are_unsunk_ships_left(current_fleet): game_over = True

    if game_over: print("Game over! You required", len(shots), "shots.")
    else: print("Sorry to see you go, come back and play anytime!")


if __name__ == '__main__': #keep this in
   main()