#hangman project
# 1.randomly choose a word from the words and assign to variable called chosen.

# 2.create an empty list display.for each letter in chosen word,add a _ to display.so if the 
# chosen word was roshan it should display 6 _,_,.... representing letter to guess.
 
# 3.check if the letter the user guessed is one of the letter in chosen word.

# 4.ask the user to guess a letter and assign to variable guess.make guess a lowercase.

# 5.loop through each position in chosen word .if the letter at that position matches "guess" 
# then reveal that letter in display at that position.

# 6.use the while loop to let the user guess again.the loop should only stop once the user has 
# guessed all the letters in the chosen and 'display' has no more blanks ("_").then you can tell
# the user they have won. 

import random

from hangmanwords import logo
print(logo)

from hangmanwords import word

chosen=random.choice(word)
print("The chosen word is : " + chosen)

display=[]

for i in range(len(chosen)):
    display+="_"
print(display)

endofgame=False

while not endofgame:
    guess=input("guess a letter : ").lower()
    
    for pos in range(len(chosen)):
        letter = chosen[pos]
        if letter == guess:
            display[pos]=letter
    print(display)
    
    if "_" not in display:
        endofgame=True
        print("you won ... ")
        
