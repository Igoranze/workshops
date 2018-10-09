"""
Hangman is a quick and easy game for at least two people that requires nothing more than paper, a pencil, and the ability to spell.
One player, the "host," makes up a secret word, while the other player tries to guess the word by asking what letters it contains.

However, every wrong guess brings them one step closer to losing.
Hangman can also be customized to make the game easier, harder, or educational, and there are apps and websites to play online if you would like.
"""
import random
import os
from __builtin__ import raw_input


hangman = (

    """
       _________
        |/        
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        """,

    """
       _________
        |/   |      
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        H""",

    """
       _________       
        |/   |              
        |   (_)
        |                         
        |                       
        |                         
        |                          
        |___                       
        HA""",

    """
       ________               
        |/   |                   
        |   (_)                  
        |    |                     
        |    |                    
        |                           
        |                            
        |___                    
        HAN""",


    """
       _________             
        |/   |               
        |   (_)                   
        |   /|                     
        |    |                    
        |                        
        |                          
        |___                          
        HANG""",


    """
       _________              
        |/   |                     
        |   (_)                     
        |   /|\                    
        |    |                       
        |                             
        |                            
        |___                          
        HANGM""",



    """
       ________                   
        |/   |                         
        |   (_)                      
        |   /|\                             
        |    |                          
        |   /                            
        |                                  
        |___                              
        HANGMA""",


    """
       ________
        |/   |     
        |   (_)    
        |   /|\           
        |    |        
        |   / \        
        |               
        |___           
        HANGMAN""")


def run():
    """
    Hangman starts here
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # First, select a random word from the hangman.txt file of words
    # Read the file
    with open('hangman.txt', 'r') as hangman_file:
        # Read all lines into a list
        lines = hangman_file.readlines()

        # Select a random line from list
        random_word = random.choice(lines)

        # The random word contains \n as break, we need to remove this break if we want to use the word, so deleting last two chars of the word
        random_word = random_word[:-1]

    # We now got our random_word, and it is now time to start guessing
    # We need some sort of game logic to see if we have died, or won.
    # We use the while loop with a predefined boolean
    game_over = False
    wrong_answers = 0
    right_answers = 0

    tmp_random_word = random_word
    for letter in alphabet:
        tmp_random_word = tmp_random_word.replace(letter, '_')

    while not game_over:
        # Print hangman's status with wrong answers
        print(hangman[wrong_answers])

        print(tmp_random_word)

        # Let the user of this game guess a char
        # We would like some logic to check if the user only enters text (String) an no special chars like !@#$%^
        guess_char = str(raw_input('Guess a char: '))

        if guess_char == '':
            guess_char = '~'

        # If user guessed wrong chard, then print hangman and update wrong answers
        if guess_char not in random_word:
            # Update wrong answers
            wrong_answers += 1
        else:
            right_answers += 1
            # If the user entered the correct answer
            # update the alphabet list
            # NOTE: This one is not really performance best, but it is simple
            new_alphabet = []
            for letter in alphabet:
                if letter is not guess_char:
                    new_alphabet.append(letter)

            alphabet = new_alphabet

        # Print the word that is guessed:
        tmp_random_word = random_word
        for letter in alphabet:
            tmp_random_word = tmp_random_word.replace(letter, '_')

        # Check if max wrong answers are given, if so then it is game over
        if len(hangman) - 1 == wrong_answers or len(random_word) == right_answers:
            game_over = True

        # At the end of the while loop, clear the console
        os.system('clear')

    print(hangman[wrong_answers])

    if len(hangman) - 1 != wrong_answers:
        print('Wow you win!')
    else:
        print('Game over!')

    print('Correct word: {}'.format(random_word))


# App runs from here in the terminal
run()
