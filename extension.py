#see the readme.md file for description and data
import battleships

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
    updates board following a hit, marking the square with "*"
    """
    board[row][col] = "*"

def update_board_miss(row, col, board):
    """
    updates board following a miss, marking the square with "-"
    """
    board[row][col] = "-"

def update_board_sink(ship_sunk, board):
    """
    updates board following the sinking of a ship, marking all squares that the ship occupied with a
    "B" if it is a battleship, "C" if it is a cruiser, "D" if it is a destroyer and "S" if it is a
    submarine
       """
    #Determine markers based on ship type
    if battleships.ship_type(ship_sunk)=="battleship":
        ship_sunk_type = "B"
    elif battleships.ship_type(ship_sunk)=="cruiser":
        ship_sunk_type = "C"
    elif battleships.ship_type(ship_sunk)=="destroyer":
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
    for i in range(10):
        print(i, "|", end=" ")
        for j in range(10)):
            if j<9: print(board[i][j], end="  ")
            else: print(board[i][j])

def main():
    """
    returns nothing. It prompts the user to call out rows and columns of shots and
    outputs the responses of the computer iteratively until the game stops. Further
    requirements: (a) there must be an option for the human player to quit the game
    at any time, (b) the program must never crash (i.e., no termination with Python
    error messages), whatever the human player does.
    """
    current_fleet = battleships.randomly_place_all_ships()

    current_board = create_board()

    game_over = False
    shots = set()

    while not game_over:
        loc_str = input("Enter row and column to shoot (separted by space) or enter q to quit: ").split()
        if loc_str==["q"]: break
        elif battleships.is_valid_input(loc_str)==False:
            print("Invalid input, please try again")
            continue
        else:
            current_row = int(loc_str[0])
            current_column = int(loc_str[1])
            if battleships.coords_already_targeted(current_row, current_column, current_board):
                print("You have already targeted these coordinates, please try again")
                continue
            else:
                shots|={(current_row, current_column)}
                if battleships.check_if_hits(current_row, current_column, current_fleet):
                    update_board_hit(current_row, current_column, current_board)
                    print("You have a hit!")
                    (current_fleet, ship_hit) = battleships.hit(current_row, current_column, current_fleet)
                    if battleships.is_sunk(ship_hit):
                        print("You sank a " + battleships.ship_type(ship_hit) + "!")
                        update_board_sink(ship_hit, current_board)
                else:
                    print("You missed!")
                    update_board_miss(current_row, current_column, current_board)

        print_board(current_board)

        if not battleships.are_unsunk_ships_left(current_fleet): game_over = True

    if game_over: print("Game over! You required", len(shots), "shots.")
    else: print("Sorry to see you go, come back and play anytime!")


if __name__ == '__main__': #keep this in
   main()