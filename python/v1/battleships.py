from python.functions import *
from python.classes import Ocean, Ship, Fleet


def main():

    # Game set up
    new_fleet = create_clean_fleet()
    o = Ocean()
    bd = randomly_place_all_ships(new_fleet, o)
    playing = bd.fleet.are_unsunk_ships_left()

    print("\n**********************")
    print("Welcome to Battleships")
    print("**********************")

    shots = 0

    while playing:

        try:

            guess = True
            while guess:

                try:
                    loc_str = input(
                        "Enter row and colum to shoot (separted by space): "
                    ).split()
                    current_row = int(loc_str[0])
                    current_column = int(loc_str[1])

                    if (
                        isinstance(current_row, int)
                        and isinstance(current_column, int)
                        and current_row <= 9
                        and current_column <= 9
                    ):
                        guess = False

                except ValueError:
                    print("Not a valid input, please try again\n")
                    continue

            shots += 1

            if bd.check_if_hits(current_row, current_column):

                hit = bd.hit(current_row, current_column)

                marker = True

                print("You have a hit!")
                bd.update_display_ocean(current_row, current_column, marker)

                if hit[3].is_sunk() is True:

                    coor = bd.get_coor_for_ship(hit[2])
                    marker = bd.hit_marker[hit[1]]

                    for a, b in coor:
                        bd.update_display_ocean(a, b, marker)

                    print("You sank a " + Ship.ship_type(hit[3], hit[3].length) + "!")

            else:
                marker = False
                print("You missed!")
                bd.update_display_ocean(current_row, current_column, marker)

            bd.pretty_print_display_ocean()
            bd.pretty_print_ocean()
            playing = bd.fleet.are_unsunk_ships_left()

        except IndexError:
            print("Whoops, please try again.\n")
            continue

    print("Player wins")
    print("\n You took {shots}".format(shots=shots))


if __name__ == "__main__":
    main()
