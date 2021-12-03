from random import randint
from python.classes import Ship, Fleet, Ocean


def create_clean_fleet():
    ships = []
    for ship in Ship.ships:
        id = Ship.ship_id[ship]
        row = None
        column = None
        horizontal_random = Ship.horizontal[randint(0, 1)]
        length = Ship.ship_length[ship]
        hits = []
        coor = []

        ships.append(
            Ship(
                id=id,
                row=row,
                column=column,
                horizontal=horizontal_random,
                length=length,
                hits=hits,
                coor=coor,
            )
        )

    fleet = Fleet(ships)

    return fleet


def is_open_sea(row, column, board):

    try:
        board = board.ocean
        marker = Ocean().marker

        if board[row][column] != marker:
            return False

        elif (
            board[row - 1][column - 1] == marker
            and board[row - 1][column] == marker
            and board[row - 1][column + 1] == marker
            and board[row][column - 1] == marker
            and board[row][column + 1] == marker
            and board[row + 1][column - 1] == marker
            and board[row + 1][column] == marker
            and board[row + 1][column + 1] == marker
        ):

            return True

        else:
            return False

    except IndexError:
        return False


def ok_to_place_ship_at(input, board):

    open_sea = [is_open_sea(x, y, board) for x, y in input]

    if False not in open_sea:
        return True

    else:
        return False


def place_ship_at(row, column, horizontal, length, board, ship):

    if horizontal is True:
        for i in range(0, length):
            board.ocean[row][i + column] = length
            ship.coor.append((str(row) + str(i + column)))
    else:
        for i in range(0, length):
            board.ocean[i + row][column] = length
            ship.coor.append((str(i + row) + str(column)))

    return board


def get_random_coor(ship):

    horizontal = ship.horizontal
    length = ship.length

    if horizontal is True:
        row_rnd = randint(0, 9)
        column_rnd = randint(0, 9 - length)
        row_col = [row_rnd, column_rnd, horizontal]

        return row_col

    elif horizontal is False:
        row_rnd = randint(0, 9 - length)
        column_rnd = randint(0, 9)
        row_col = [row_rnd, column_rnd, horizontal]

        return row_col


def get_first_last_coor(ship, random_coor):

    ship_coor = random_coor
    length = ship.length

    if length == 1:
        coor1 = [ship_coor[0]]
        coor2 = [ship_coor[1]]
        ship_coor = zip(coor1, coor2)

        return ship_coor

    elif ship_coor[2] is True:

        coor1 = [ship_coor[0], ship_coor[0]]
        coor2 = [ship_coor[1], ship_coor[1] + length]
        ship_coor = zip(coor1, coor2)

        return ship_coor

    else:
        coor1 = [ship_coor[0], ship_coor[0] + length]
        coor2 = [ship_coor[1], ship_coor[1]]
        ship_coor = zip(coor1, coor2)

        return ship_coor


def randomly_place_all_ships(fleet, ocean):

    ship_list = []

    for ship in fleet.fleet:

        place_ship = True

        while place_ship:

            random_coor = get_random_coor(ship)
            ship_coor = get_first_last_coor(ship, random_coor)
            valid_pos = ok_to_place_ship_at(ship_coor, ocean)

            if valid_pos is True:

                ship.row = random_coor[0]
                ship.column = random_coor[1]
                place_ship_at(
                    row=ship.row,
                    column=ship.column,
                    horizontal=ship.horizontal,
                    length=ship.length,
                    board=ocean,
                    ship=ship,
                )
                ship_list.append(ship)
                place_ship = False

            else:
                continue

    fleet = Fleet(ship_list)
    ocean.fleet = fleet

    return ocean
