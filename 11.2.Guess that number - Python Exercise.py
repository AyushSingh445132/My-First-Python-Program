# Create a Program to guess a given number
# Rerun the program to a specific number of turns
# After every turn print whether the typed number is "greater" or "lesser" than the number to be found
# If the user cannot guess the number after all turns are finished print "Game Over"
# If the user won print the number of guesses user took to finish it.

# guess the number
n = 18
# nog = number_of_guesses
nog = 1
print("You will get 5 chances to guess the correct number")

while (nog<=5):
# gn = guess_number
      gn = int(input("Enter Number:\n"))
      if gn<n:
            print("Sorry!! wrong number.Guess a number greater than this\n")
      elif gn>n:
            print("Sorry!! wrong number.Guess a number smaller than this\n")
      else :
            print("Congratulation you won the Game")
            print("You have guessed the correct number")
            print("You took" , nog , "guess to finish the game")
            break
      print(5-nog, "guesses left")
      nog = nog + 1

if (nog>5):
    print("Game Over\n")
    print("You could not guess the number")



