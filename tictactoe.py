"""
A simple game using a small 3X3 graph of empty boxes.
Players alternate turns by placing a single 'X' or 'O' into an empty box.
The first player to get 3 X's or O's lined up horizontally, vertically, or diagonally, wins the game (a line is often drawn through the 3 winning icons).
If each player is smart enough the game will always end in a draw, otherwise known as a "cat's-tail".
"""
import os
from __builtin__ import raw_input

grid_game_winner_combo = [
    ['1', '2', '3'],
    ['1', '4', '7'],
    ['1', '5', '9'],

    ['2', '5', '8'],

    ['3', '5', '7'],
    ['3', '6', '9'],

    ['4', '5', '6'],

    ['7', '8', '9'],
]


def run():
    # First column is 7, second is 13 and third is is 19
    game_layout = """
                |       |
            1   |   2   |   3    
        --------|-------|--------
                |       |
            4   |   5   |   6    
        --------|-------|--------
            7   |   8   |   9    
                |       |        
        """

    # We need to keep track of the players movements
    choices_player_x = []
    choices_player_y = []

    # We need some sort of game logic loop
    # Using while loop with game_over boolean
    game_over = False
    while not game_over:
        # Clear screen
        os.system('clear')

        # Print the game bord
        print(game_layout)

        # Always start with player x
        print('Player X it is your turn!')

        # Need logic to check if input is integer
        choice_x = str(raw_input('Whats your move?\nPut in the number from the game bord: '))

        # Save choice in player_x
        choices_player_x.append(choice_x)

        # Replace the number from the bord with the move of player X
        # Fix so that it is not possible to overwrite other players move
        game_layout = game_layout.replace(choice_x, 'X')

        # Clear screen
        os.system('clear')

        # Check if player_x has won
        for winner_combos in grid_game_winner_combo:
            combo = 0
            for winner_combo in winner_combos:
                if winner_combo in choices_player_x:
                    combo += 1
            if combo == 3:
                print('Player X won woot!')
                game_over = True

        # Print the game bord
        print(game_layout)

        if game_over:
            break

        print('Player Y it is your turn!')

        # Need logic to check if input is integer
        choice_y = str(raw_input('Whats your move?\nPut in the number from the game bord: '))

        # Save choice in player_y
        choices_player_y.append(choice_y)

        # Replace the number from the bord with the move of player X
        # Fix so that it is not possible to overwrite other players move
        game_layout = game_layout.replace(choice_y, 'Q')

        # Check if player_y has won
        for winner_combos in grid_game_winner_combo:
            combo = 0
            for winner_combo in winner_combos:
                if winner_combo in choices_player_y:
                    combo += 1
            if combo == 3:
                print('Player Y won woot!')
                game_over = True

        if game_over:
            break


run()
