import random

NUMBER_ROWS = 6
NUMBER_COLS = 12

def make_list(number_rows, number_cols):
    seats = []
    for row in range(0, number_rows):
        seats.append([])
        for seat in range(0, number_cols):
            seats[row].append(False)
    return seats

def print_list(seat_list):
    for row in seat_list:
        for seat in row:
            full = ' '
            if seat:
                full = 'x'
            print(f'[{full}]', end="")
        print("")

def fill_seat(row, column, seat_list):
    seat_list[row][column] = True

def fill_random_seats(seat_list):
    number_rows = len(seat_list)
    number_cols = len(seat_list[0])

    num_full = random.randint(5, 70)

    for _ in range(num_full):
        running = True
        while running:
            row = random.randint(0, number_rows - 1)
            column = random.randint(0, number_cols - 1)
            if not seat_list[row][column]:
                running = False

        fill_seat(row, column, seat_list)

seat_list = make_list(NUMBER_ROWS, NUMBER_COLS)
fill_random_seats(seat_list)
print_list(seat_list)