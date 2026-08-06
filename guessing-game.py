import random

computer_select = random.randint(1, 10)

total_guess = 0
wrong_guess = 0

while True:
    # print("Enter the Number: ")
    user_guess = int(input("Enter the Number to Guess: "))
    if user_guess>computer_select:
        print("Guess is high than computer selected")
        print("enter lower number")
        wrong_guess+=1

    elif user_guess<computer_select:
        wrong_guess+=1
        print("guess is close low")
    elif user_guess==computer_select:
        print("Congragulation you guessed the number in ",wrong_guess+1," attempts")
        break