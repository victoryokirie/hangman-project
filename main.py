
import random
import hangman_word
from hangman_art import logo, stages
import os



word_list=hangman_word

#randomly choosing a word from a huge long list of words
chosen_word=random.choice(hangman_word.word_list)
print(chosen_word)

#player has 6 lives at the start of the game
lives=6

print(logo)

# Creating a blank list and populating it with "-"" corresponding to chosen word length
display = []
for letter in range(len(chosen_word)):
    display.append("-")


#initial game status
end_of_game=False

while not end_of_game:
    #asking player to guess a letter in the chosen word
    guess= input("please guess a letter in the word...:").lower()

    if guess in display:
      print(f"You've already guessed {guess}")
    
    os.system('cls')


    #checking if the guessed letter is in the chosen word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position]= letter
        
    #checking if the user failed to guess correctly and reducing user's life
    if guess not in chosen_word:
        print(f"you've guessed {guess} and it is not in the word. you've lost a life")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose")
   

    print(f"{''.join(display)}")

    # Check if user has guessed all the letters
    if "-" not in display:
        end_of_game= True
        print("You win")
    
    
    print(stages[lives])





