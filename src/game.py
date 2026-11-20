from functions import greeting, generate_word, synonym, definition

"""
Greet the user
"""

greeting()

continue_game = input("Would you like to continue playing the game? (yes/no): ")

if continue_game.lower() == "yes":
    print(f"\nGreat! Let's continue playing the game.\n\n")
else:
    print("Thank you for playing the game. Goodbye!")
    exit()

"""
Present the user with a random word 
"""

print(f'The random word that has been generated is: {generate_word()}\n\n')
print(f"You will now have to guess any synonym of the given word\n\n")

"""
Return the synonym of the random word generated
It is returned as a list
if any of the guesses match the synonyms of the list, the user will be informed that they have guessed correctly
Otherwise the user will be given a strike and informed that they have guessed incorrectly
"""

synonyms = synonym() 

"""NOTE: This is a test to check if its generating the right synonyms"""
print(synonyms)
strikes = 0

while True:
    guess = input("Please enter your guess for a synonym of the given word: ")

    if guess in synonyms:
        print("Congratulations! You have guessed correctly!")
        break
    else:
        strikes += 1
        print("Sorry, that is incorrect. You have been given a strike.")
        print(f"You have {strikes} strikes. You have a maximum of 10 strikes, so be careful!")

    if strikes == 10:
        print("Sorry, you have reached the maximum number of strikes. Game over!")
        break