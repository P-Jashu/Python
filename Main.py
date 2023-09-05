import random

#Printing logo
from HangMan_Art import logo
print(logo)

#choosing a word from list of words
from HangMan_Word import word_list
RanWord = random.choice(word_list)
Wl = len(RanWord)
game_over = False
lives = 6

#creating a list to show guessed words
Result = []
for _ in RanWord:
    Result += "_"

#logic of game
while not game_over:
    #input from user
    guess = input("\nGuess a letter: ").lower()
    if guess in Result:
        print(f"You have already guessed the letter({guess})")

    #checking if it is right
    for i in range(Wl):
        if RanWord[i] == guess:
            Result[i] = guess
    print(Result)
    print("Your guess was right")

    #checking if it is wrong
    if guess not in RanWord:
        print(f"Your guess {guess} is wrong!!")
        lives -= 1 
        from HangMan_Art import stages
        print(stages[lives])
        print(f"\nYour remaining lives are: {lives}")
        if lives == 0:
            game_over = True
            print(f"The word was '{RanWord}'\n")
            print("You lost the game!!")

    #winning statement
    if "_" not in Result:
        print("Congratulations, You Won the game")