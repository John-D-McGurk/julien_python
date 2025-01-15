import journal.journal as journal
import calculator.calculator as calc
import login.login as login


user = login.pick()


while True:
    command = input("₱ ").strip()

    if command == "journal":
        journal.start()

    elif command == "calc":
        calc.calculate()

    elif command == "quit":
        break

    else:
        print(f"Command not found: {command}")
