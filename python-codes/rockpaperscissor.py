import random

choices=['rock','paper','scissors']

#keeping track of scores.
userScore=0
compScore=0

while True:
    user_input= input("choose from: rock, paper or scissors: ").lower() #ensures input is in lowercase

    computer_input= random.choice(choices)

    print(f"\n You chose {user_input} and the computer chose {computer_input}.\n")

    if user_input not in choices:
        print("Invalid choice, Please try again.")
        continue

    if user_input==computer_input:
        print("Looks like you both have opted for similar option. Its a tie!")
    elif (user_input == "rock" and computer_input == "scissors"):
        print("Way to go! You win!")
        userScore += 1
    elif(user_input == "paper" and computer_input == "rock"):
        print("Way to go! You win!")
        userScore += 1
    elif(user_input == "scissors" and computer_input == "paper"):
        print("Way to go! You win!")
        userScore += 1

    else:
        print(" You Lose. Better luck next time.")
        compScore +=1

    print(f"Scores: You {userScore} - Computer {compScore}")

    playagain = input("Do you wish to play again? (yes/no): ").lower()
    if playagain != "yes":
        print("Thanks for playing!")
        break


    

