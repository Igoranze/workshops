def fizzbuzz(number):
    # is het nummer deelbaar door 3 en door 5? print fizzbuzz
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    # is het nummer deelbaar door 3? print fizz
    elif number % 3 == 0:
        print('Fizz')
    # is het nummer deelbaar door 5? print buzz
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

# loop door 100 nummers
for number in range(1, 101):
    fizzbuzz(number)
