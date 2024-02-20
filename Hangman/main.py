
import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

random_word = random.choice(word_list)
out_field = ["_" for indx in range(0, len(random_word))]
lives_rem = 6
had_won = False

while(lives_rem >= 0 and not had_won):
    print(" ".join(out_field))
    usr_guess = input("Guess a word: ")

    if(usr_guess in out_field):
        print(f"You already guessed {usr_guess}. Try a different word!!")
    elif(len(usr_guess) > 1):
        print("Invalid Input!!")
    else:
        if(usr_guess not in random_word):
            print(f'You guessed {usr_guess}, that\'s not in the word.'
                + '\nYou lose a life.')
            print(stages[lives_rem])
            lives_rem -= 1

        else:
            for indx in range(0, len(random_word)):
                if(usr_guess == random_word[indx]):
                    out_field[indx] = usr_guess

    out = "".join(out_field)
    if(out == random_word):
        had_won = True
        print(out)
        print("You win!!")

if(lives_rem == 0):
    print("You lost all your lives.")
    print("You Lose!!")