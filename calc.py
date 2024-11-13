

def get_number():
    try:
        user_input = int(user_input("Enter first number: "))
    except ValueError:
        print("That isnt a number. Try again.")
        user_input = get_number()
    return user_input


number_1 = get_number()
number_2 = get_number()
