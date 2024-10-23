import random

choices = ["rock", "paper", "scissors"]
computer_choice =  random.randint(0,2)

computer_choice_as_string = choices[computer_choice]

user_choice = input("Enter rock, paper or scissors: ")

if computer_choice_as_string == user_choice:
    print("Draw!")
elif computer_choice_as_string == "paper":
    if user_choice == "rock":
        print("You lose!")

print(computer_choice_as_string)