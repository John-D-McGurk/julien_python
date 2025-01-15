def get_number():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        print("Not a number!")
        return get_number()
    
def calculate():    
    num_1 = None
    while True:
        if num_1 is None:
            num_1 = get_number()
        operator = input("Enter +, -, /, * or =: ")
        if operator == "=":
            print(num_1)
            break
        num_2 = get_number()
        if operator == "+":
            num_1 = num_1 + num_2
        elif operator == "-":
            num_1 = num_1 - num_2
        elif operator == "/":
            num_1 = num_1 / num_2
        elif operator == "*":
            num_1 = num_1 * num_2
