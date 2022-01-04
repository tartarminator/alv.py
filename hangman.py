from random import choice
from IPython.display import clear_output

words = ["tree", "basket", "chair", "paper", "python"]
word = choice(words)
guessed, lives, game_over = [], 7, False

guesses = ["_ "] * len(word)

while not game_over:
    hidden_word = "".join(guesses)
    print("Your guessed letters: {}".format(guessed))
    print("Word to guess: {}".format(hidden_word))
    print("Lives: {}".format(lives))

    ans = input("Type quit or guess a letter: ").lower()

    clear_output()

    if ans == "quit":
        print("Thanks for playing.")
        game_over = True
    elif ans in word and ans not in guessed:
        print("You guessed correctly!")

        for i in range(len(word)):
            if word[i] == ans:
                guesses[i] = ans
    elif ans in guessed:
        print("You already guessed that. Try again.")
    else:
        lives -= 1
        print("Incorrect, you lost a life.")
    if ans not in guessed:
         guessed.append(ans)

    if lives <= 0:
        print("You lost all your lives, you lost!")
        game_over = True
    elif word == "".join(guesses):
        print("Congratulations, you guessed it correctly!")
        game_over = True
