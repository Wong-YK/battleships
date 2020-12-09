#see the readme.md file for description and data

def is_sunk(ship):
    return ship[3]==len(ship[4])

def ship_type(ship):
    if ship[3]==4:
        return "battleship"
    elif ship[3]==3:
        return "cruiser"
    elif ship[3]==2:
        return "destroyer"
    else:
        return "submarine"

def is_open_sea(row, column, fleet):
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
    fleet.append((row, column, horizontal, length, {}))
    return fleet

def randomly_place_all_ships():
    #remove pass and add your implementation
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
    ship_coords = set()
    for ship in fleet:
        if ship[2]:
            for i in range(ship[3]):
                ship_coords |= {(ship[0], ship[1] + i)}
        else:
            for i in range(ship[3]):
                ship_coords |= {(ship[0] + i, ship[1])}
    print(ship_coords)
    print(len(ship_coords))
    hit = False
    for coord in ship_coords:
        if row==coord[0] and column==coord[1]:
            hit = True
        else: continue
    return hit

def hit(row, column, fleet):
    #remove pass and add your implementation
    pass

def are_unsunk_ships_left(fleet):
    #remove pass and add your implementation
    pass

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()    
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_shis_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
