

def make_list(number_rows, number_cols):
    seats = []
    for row in range(0, number_rows):
        seats.append([])
        for seat in range(0, number_cols):
            seats[row].append(False)
    return seats
    

seat_list = make_list(6, 10)

for row in seat_list:
    print(row)