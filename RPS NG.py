import random
print(" ---------------------")
print("| Rock Paper Scissors |")
print(" ---------------------")
listCh = ["R", "P", "S"]
userScore = 0
computerScore = 0
i = 1
chance = int(input("How many time you want to play (no. of chances): "))
while i <= chance:
    computerCh = str(random.choice(listCh))
    userCh = input("Enter Rock, Paper, Scissors (key to press: R,P,S): ").upper()
    if userCh == computerCh:
        print("Tie You Both Entered Same")
    elif userCh == "R":
        print("Computer Enter: ", computerCh)
        if computerCh == "P":
            print("you lose! Paper covers Rock")
            computerScore += 1
        else:
            print("you win! Rock smashes Scissors")
            userScore += 1
    elif userCh == "P":
        print("Computer Enter: ", computerCh)
        if computerCh == "S":
            print("you lose! Scissor cut Paper")
            computerScore += 1
        else:
            print("you win! Paper covers Rock")
            userScore += 1
    elif userCh == "S":
        print("Computer Enter: ", computerCh)
        if computerCh == "R":
            print("you lose! Rock smashes Scissors")
            computerScore += 1
        else:
            print("you win! Scissor cut Paper")
            userScore += 1
    else:
        print(":(")
    print("\n\t******ScoreBoard******")
    print(f"\t You: {userScore} | Computer: {computerScore}")
    print("\t**********************")
    print(f"Game No:[{i}]")
    print("========================================================")
    i += 1
print("\n\n##### Game Over #####")
print("*******************************************")
if userScore < computerScore:
    print(
        "sorry You lose the game \n computer win the game with score:", computerScore
    )
elif userScore == computerScore:
    print("Game is Tie Play Again")
else:
    print("You Win the Game with score:", userScore)
