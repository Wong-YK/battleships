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
    ship_squares=set()
    for ship in fleet:
        if ship[2]:
            for i in range(-1, ship[3]+1):
                ship_squares|={(ship[0], (ship[1]+i)), ((ship[0]-1), (ship[1]+i)), ((ship[0]+1), (ship[1]+i))}
        else:
            for i in range(-1, ship[3]+1):
                ship_squares|={((ship[0]+i), ship[1]), ((ship[0]+i), (ship[1]-1)), ((ship[0]+i), (ship[1]+1))}
    if (row, column) in ship_squares: return False
    else: return True

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """
    checks if addition of a ship, specified by row, column, horizontal, and
    length as in ship representation above, to the fleet results in a legal
    arrangement (see the figure above). If so, the function returns Boolean
    True and it returns False otherwise. This function makes use of the function
    is_open_sea
    """
    ship_coords = set()
    if horizontal:
        for i in range(length):
            ship_coords|={(row, column+i)}
    else:
        for i in range(length):
            ship_coords|={(row+i, column)}
    ok = True
    for coord in ship_coords:
        if coord[0]<0 or coord[0]>9: ok = False
        if coord[1]<0 or coord[1]>9: ok = False
        if not is_open_sea(coord[0], coord[1], fleet): ok = False
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
    f = []
    lengths = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for length in lengths:
        # find a legal placement
        placement_legal = False
        while not placement_legal:
            row = random.randrange(0, 10)
            col = random.randrange(0, 10)
            h = random.choice([True, False])
            placement_legal = ok_to_place_ship_at(row, col, h, length, f)
        # add ship to fleet
        f = place_ship_at(row, col, h, length, f)
    return f

def check_if_hits(row, column, fleet):
    """
    returns Boolean value, which is True if the shot of the human player at the square
    represented by row and column hits any of the ships of fleet, and False otherwise
    """
    ship_coords = set()
    for ship in fleet:
        if ship[2]:
            for i in range(ship[3]):
                ship_coords |= {(ship[0], ship[1] + i)}
        else:
            for i in range(ship[3]):
                ship_coords |= {(ship[0] + i, ship[1])}
    hit = False
    for coord in ship_coords:
        if row==coord[0] and column==coord[1]:
            hit = True
        else: continue
    return hit

def hit(row, column, fleet):
    """
    returns a tuple (fleet1, ship) where ship is the ship from the fleet fleet that
    receives a hit by the shot at the square represented by row and column, and fleet1
    is the fleet resulting from this hit. It may be assumed that shooting at the square
    row, column results in hitting of some ship in fleet
    """
    for ship in fleet:
        ship_coords = set()
        if ship[2]:
            for i in range(ship[3]):
                ship_coords |= {(ship[0], ship[1] + i)}
        else:
            for i in range(ship[3]):
                ship_coords |= {(ship[0] + i, ship[1])}
        if (row, column) in ship_coords:
            i = fleet.index(ship)
            fleet[i][4].add((row, column))
            return (fleet, ship)

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
    input_list_copy = copy.deepcopy(input_list)
    input_valid = True
    try:
        for i in range(len(input_list_copy)):
            input_list_copy[i]=int(input_list_copy[i])
        if len(input_list_copy) > 2 or input_list_copy[0] < 0 or input_list_copy[0] > 9 or input_list_copy[1] < 0 or input_list_copy[1] > 9:
                input_valid = False
    except:
        input_valid = False
    return input_valid

def coords_already_targeted(row, column, board):
    already_targeted = False
    markers = ["-", "*", "B", "C", "D", "S"]
    for marker in markers:
        if board[row][column]==marker:
            already_targeted = True
    return already_targeted

def create_board():
    """
    returns list of lists that serves as a  representation of the game board
    in its initial state (i.e. no shots fired); this representation will be
    used for the graphics element of the game
    """
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(10)]
    return board

def update_board_hit(row, col, board):
    """"
    returns list of lists to represent updated game board following a hit which
    is denoted by a "*"
    """
    board[row][col] = "*"

def update_board_miss(row, col, board):
    """
    returns list of lists to represent updated game board following a miss which
    is denoted by a "-"
    """
    board[row][col] = "-"

def update_board_sink(ship_sunk, board):
    """
    returns list of lists to represent updated game board following a sink which
    is denoted by a "B" if a battleship is sunk, a "C if a cruiser is sunk, a
    "D" if a destroyer is sunk and a "S" if a submarine is sunk
       """
    #Determine markers based on ship type
    if ship_type(ship_sunk)=="battleship":
        ship_sunk_type = "B"
    elif ship_type(ship_sunk)=="cruiser":
        ship_sunk_type = "C"
    elif ship_type(ship_sunk)=="destroyer":
        ship_sunk_type = "D"
    else:
        ship_sunk_type = "S"

    #Apply markers to board
    for (row, col) in ship_sunk[4]:
        board[row][col] = ship_sunk_type

def print_board(board):
    """
    prints representation of game board along with column and row markers
    """
    print("\t"+"0  1  2  3  4  5  6  7  8  9")
    print("\t"+"-"*28)
    for i in range(len(board)):
        print(i, "|", end=" ")
        for j in range(len(board[i])):
            if j<9:
                print(board[i][j], end="  ")
            else:
                print(board[i][j])

def main():
    """
    returns nothing. It prompts the user to call out rows and columns of shots and
    outputs the responses of the computer iteratively until the game stops. Further
    requirements: (a) there must be an option for the human player to quit the game
    at any time, (b) the program must never crash (i.e., no termination with Python
    error messages), whatever the human player does.
    """
    current_fleet = randomly_place_all_ships()

    current_board = create_board()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and column to shoot (separted by space) or enter q to quit: ").split()
        if loc_str==["q"]: break
        elif is_valid_input(loc_str)==False:
            print("Invalid input, please try again")
            continue
        else:
            current_row = int(loc_str[0])
            current_column = int(loc_str[1])
            if coords_already_targeted(current_row, current_column, current_board):
                print("You have already targeted these coordinates, please try again")
                continue
            else:
                shots += 1
                if check_if_hits(current_row, current_column, current_fleet):
                    update_board_hit(current_row, current_column, current_board)
                    print("You have a hit!")
                    (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                    if is_sunk(ship_hit):
                        print("You sank a " + ship_type(ship_hit) + "!")
                        update_board_sink(ship_hit, current_board)
                else:
                    print("You missed!")
                    update_board_miss(current_row, current_column, current_board)

        print_board(current_board)

        if not are_unsunk_ships_left(current_fleet): game_over = True

    if game_over: print("Game over! You required", shots, "shots.")
    else: print("Sorry to see you go, come back and play anytime!")


if __name__ == '__main__': #keep this in
   main()