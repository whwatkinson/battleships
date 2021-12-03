from typing import List, Optional


class Ocean:
    """
    docstring here
    """

    row_size = 10
    col_size = 10
    marker = '.'

    hit_marker = {'hit': '*', 'miss': '-', 'submarine': 'S', 'destroyer': 'D', 'cruiser': 'C', 'battleship': 'B'}


    def get_coor_for_ship(self, input):

        coor = input
        coor_joined = ''.join(coor)

        x = []
        y = []

        for i in range(0, len(coor_joined)):
            if i % 2 == 0:
                x.append(int(coor_joined[i]))
            else:
                y.append(int(coor_joined[i]))

        result = zip(x, y)

        return result

    def update_display_ocean(self, row, column, marker):

        if marker is True:
            self.display_ocean[row][column] = self.hit_marker['hit']

        elif marker is False:
            self.display_ocean[row][column] = self.hit_marker['miss']

        elif marker == 'B':
            self.display_ocean[row][column] = self.hit_marker['battleship']

        elif marker == 'C':
            self.display_ocean[row][column] = self.hit_marker['cruiser']

        elif marker == 'D':
            self.display_ocean[row][column] = self.hit_marker['destroyer']

        elif marker == 'S':
            self.display_ocean[row][column] = self.hit_marker['submarine']

        else:
            print('WIP')

    def hit(self, row, column):

        shot = str(row) + str(column)
        coor = [(x.id, x.coor, x.length) for x in self.fleet.fleet]
        hit_miss = [(x[0], x[2]) for x in coor if shot in x[1]]

        if hit_miss != []:
            id = hit_miss[0][0]
            hit = hit_miss[0][1]
            self.fleet.fleet[id].hits.append(shot)
            result = (self, self.fleet.fleet[id].ship_type(hit), self.fleet.fleet[id].coor, self.fleet.fleet[id])

            return result

        else:
            return self

    def check_if_hits(self, row, column):
        return self.ocean[row][column] != self.marker

    def create_ocean(self):
        return [[self.marker] * self.col_size for x in range(self.row_size)]

    def pretty_print_ocean(self):
        print("\n   " + "  ".join(str(x) for x in range(0, self.col_size)))
        for r in range(self.row_size):
            print(str(r) + "  " + "  ".join(str(c) for c in self.ocean[r]))
        print()


    def pretty_print_display_ocean(self):
        print("\n   " + "  ".join(str(x) for x in range(0, self.col_size)))
        for r in range(self.row_size):
            print(str(r) + "  " + "  ".join(str(c) for c in self.display_ocean[r]))
        print()

    def __init__(self, ocean=None, fleet=None):
        self.fleet = fleet
        if ocean is None:
            self.ocean = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

            self.display_ocean = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]


class Ship:
    """
    docstring here
    """
    ships = ['battleship', 'cruiser1', 'cruiser2', 'destroyer1', 'destroyer2', 'destroyer3', 'submarine1', 'submarine2', 'submarine3', 'submarine4']
    ship_identity = {4: 'battleship', 3: 'cruiser', 2: 'destroyer', 1: 'submarine'}
    ship_length = {'battleship': 4, 'cruiser1': 3, 'cruiser2': 3, 'destroyer1': 2, 'destroyer2': 2, 'destroyer3': 2, 'submarine1': 1, 'submarine2': 1,
                   'submarine3': 1, 'submarine4': 1}

    ship_id = {'battleship': 0, 'cruiser1': 1, 'cruiser2': 2, 'destroyer1': 3, 'destroyer2': 4, 'destroyer3': 5, 'submarine1': 6, 'submarine2': 7,
               'submarine3': 8, 'submarine4': 9}

    horizontal = [True, False]

    def is_sunk(self):
        return self.length == len(self.hits)

    def ship_type(self, ship_length):
        """returns one of the strings `"battleship"`, `"cruiser"`, `"destroyer"`, or `"submarine"` identifying the type of `ship`"""
        return self.ship_identity[ship_length]

    def __init__(self, id: int, row: Optional[int], column: Optional[int], horizontal: bool, length: int, hits: List[str], coor: List[str]):
        self.id = id
        self.row = row
        self.column = column
        self.horizontal = horizontal
        self.length = length
        self.hits = hits
        self.coor = coor

    def __repr__(self):
        return str((self.id, self.row, self.column, self.horizontal, self.length, self.hits, self.coor))

class Fleet:
    """
    doctring here
    """

    def are_unsunk_ships_left(self):
        """returns Boolean value, which is `True` if there are ships in the fleet that are still not sunk, and `False` otherwise"""

        is_sunk = [False if ship.is_sunk() else True for ship in self.fleet]

        if True in is_sunk:
            return True
        else:
            return False

    def __init__(self, fleet: List[Ship]):
        self.fleet = fleet
