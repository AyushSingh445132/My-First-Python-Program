# snake water gun

# rule
# Snake vs. Water: Snake drinks the water hence wins.
# Water vs. Gun: The gun will drown in water, hence a point for water
# Gun vs. Snake: Gun will kill the snake and win.

import random

print("|Welcome to the Game|")
print("|Snake Water Gun|")

listShape = ["S", "W", "G"]

userScore = 0
computerScore = 0

number_of_Turns = int(input("How many times you wanna play this game? "))

i = 1

while i <= number_of_Turns:
    computerShape = str(random.choice(listShape))
    userShape = input("Enter S for Snake\nEnter W for Water\nEnter G for Gun\n").upper()
    if userShape == computerShape:
        print("Tie You Both choose same Shape")

    elif computerShape == "W" and userShape == "S":
        print("Computer Chose", computerShape)
        print("👉 Snake Drank Water")
        userScore += 1

    elif computerShape == "S" and userShape == "W":
        print("Computer Chose", computerShape)
        print("👉 Snake Drank Water")
        computerScore += 1

    elif computerShape == "G" and userShape == "W":
        print("Computer Chose", computerShape)
        print("👉 Gun Drowned in Water")
        userScore += 1

    elif computerShape == "W" and userShape == "G":
        print("Computer Chose", computerShape)
        print("👉 Gun Drowned in Water")
        computerScore += 1

    elif computerShape == "S" and userShape == "G":
        print("Computer Chose", computerShape)
        print("👉 Gun Shot the Snake")
        userScore += 1

    elif computerShape == "G" and userShape == "S":
        print("Computer Chose", computerShape)
        print("👉 Gun Shot the Snake")
        computerScore += 1

    else:
        print(":( Error Input!! Try Again")

    print(f"\nGame No:[{i}]")
    print("\t******ScoreBoard******")
    print(f"\t You: {userScore} | Computer: {computerScore}")
    print("\t**********************")
    print("========================================================")
    i += 1

print("\n##### Game Khatam Paisa Hajam #####")
print("*******************************************")

if userScore < computerScore:
    print(f"😭 Sorry You lose the game 😭\n computer won the "
          f"game with {computerScore} score")

elif userScore > computerScore:
    print(f"😄 You won the Game with {userScore} score 😄")

else:
    print("😅 Game is Tie Play Again 😅")