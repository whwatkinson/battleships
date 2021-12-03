from functions import *


class TestBattleship:
    ship_0 = Ship(0, 0, 0, True, 4, ['00'], ['00', '01', '02', '03'])
    ship_1 = Ship(1, 2, 2, True, 3, [], ['22', '23', '24'])
    ship_2 = Ship(2, 5, 0, False, 3, [], ['50', '60', '70'])
    ship_3 = Ship(3, 8, 6, True, 2, ['87', '86'], ['86', '87'])
    ship_4 = Ship(4, 4, 5, False, 2, [], ['45', '55'])
    ship_5 = Ship(5, 0, 6, True, 2, ['06', '07'], ['06', '07'])
    ship_6 = Ship(6, 5, 7, True, 1, [], ['57'])
    ship_7 = Ship (7, 5, 2, False, 1, ['52'], ['52'])
    ship_8 = Ship(8, 8, 2, False, 1, [], ['82'])
    ship_9 = Ship (9, 2, 0, False, 1, ['20'], ['20'])

    test_fleet = Fleet([ship_0, ship_1, ship_2, ship_3, ship_4, ship_5, ship_6, ship_7, ship_8, ship_9])

    def test_is_sunk(self):
        test_fleet = self.test_fleet
        test_result = [ship.is_sunk() for ship in test_fleet.fleet]

        expected_result = [False, False, False, True, False, True, False, True, False, True]
        test_cases = zip(test_result, expected_result)

        for case in test_cases:
            assert case[0] == case[1]

    def test_ship_type(self):
        test_fleet = self.test_fleet
        test_result = [x.ship_type(x.length) for x in test_fleet.fleet]
        expected_result = ['battleship', 'cruiser', 'cruiser', 'destroyer', 'destroyer', 'destroyer', 'submarine',  'submarine', 'submarine', 'submarine']

        test_cases = zip(test_result, expected_result)

        for case in test_cases:
            assert case[0] == case[1]

    def test_is_open_sea(self):

        test_cases_1 = [(1, 1), (1, 2), (1, 3), (7, 7)]
        test_board = Ocean()
        test_board.ocean[1][1] = 1
        test_results = [is_open_sea(a, b, test_board) for a, b in test_cases_1]
        expected_result = (False, False, True, True)

        test_cases = zip(test_results, expected_result)

        for case in test_cases:
            assert case[0] == case[1]

    def test_are_unsunk_ships_left(self):
        test_fleet = self.test_fleet

        assert test_fleet.are_unsunk_ships_left() is True

    def test_place_ship(self):

        ship_1 = Ship(0, 2, 1, True, 1, [], [])
        ship_2 = Ship(1, 4, 4, True, 1, [], [])
        ship_3 = Ship(2, 7, 7, False, 2, [], [])
        test_fleet1 = Fleet([ship_1, ship_2, ship_3])

        board = Ocean()

        for ship in test_fleet1.fleet:
            test_board = place_ship_at(ship.row, ship.column, ship.horizontal, ship.length, board, ship)

        expected_board = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', 1, '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', 1, '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', 2, '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', 2, '.', '.'],
                          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

        assert test_board.ocean == expected_board
