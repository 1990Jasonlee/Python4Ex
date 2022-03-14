from random import randrange


def high_low():
    global random_number
    random_number = randrange(10)
    while True:
        guess = int(input('Your guess between 1-10 is: '))
        if random_number > guess:
            print(f'Your guess was {guess}.\n Too low.')
        elif random_number < guess:
            print(f'Your guess was {guess}.\n Too high.')
        elif random_number == guess:
            print(f'Your guess was {guess}.\n You guessed it correctly.')
            print(f' The random number was: {random_number}.')
            break

high_low()
