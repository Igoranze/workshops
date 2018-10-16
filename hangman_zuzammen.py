# Together
# GUI
# Use Cases

def hangman():
    # Begin: have random word to guess
    rand_word = "awesome"
    tmp_random_word = rand_word

    max_retries = 10

    # Core: guess letters and see if they are in word
      # keep count of retries
      # user input
      # Guess word or continue guessing
          # type checking, edge cases???
          # errors or continue with error message

    win = False
    while max_retries > 0:
        print('word is : ' + str(len(rand_word)) + ' long')
        input_user = input('input plx: ')

       # functions can be make from this ugly thing
        if not isinstance(input_user, str):
            print('mag niet')
            max_retries = max_retries - 1
            continue

        if len(input_user) > 1:
            # check word
            if input_user == rand_word:
                win = True
                break
            else:
                print('helaas loser sukkel')
        else:
            # check char
            if rand_word.find(input_user) >= 0:
                # TODO: print not found leteters with  _
                tmp_random_word = tmp_random_word.replace(input_user, '')

                if len(tmp_random_word) == 0:
                    win = True
                    break
                else:
                    print('You have: ' + str(len(tmp_random_word)) + ' letters over... noob')
            else:
                print('helaas loser, sukkel')

        max_retries = max_retries - 1

    # End: Win or lose check
       # Play again

    if win:
        print('Good job, hoera!!')
    else:
        print('loser')

    input_yes_no = input('Play again? y/n')
    return input_yes_no


play_again = 'y'
while play_again == 'y':
    play_again = hangman()

