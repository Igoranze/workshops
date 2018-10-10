from random import randrange

# pick random number between 1 and 100
number_to_guess = randrange(1,101)

# set retry count
retries_left = 10

print('Guess the number (1-100)!')

while (retries_left > 0):
    # ask for input
    guess = int(input('Your guess: '))
    # check given answer
    if guess == number_to_guess:
        # guess was correct, print win message
        print('YOU WIN!')
        break
    elif guess < number_to_guess:
        print('Your guess was too low!')
    elif guess > number_to_guess:
        print('Your guess was too high!')
    # deduct a retry from count
    retries_left = retries_left - 1

# all retries were used up, print lose message
if retries_left < 1:
    print('YOU LOSE!')
