import random

lower = 1
upper = 100


def main():
    print("Welcome to the HI - LO game")
    number = random.randint(lower, upper)
    choice = get_choice()
    while choice != number:
        if choice > number:
            print("Too high!")
        else:
            print("Too low!")

        choice = get_choice()
    print('Got it: The number is {}'.format(number))


def get_choice():
    return int(input('Guess a number between {} & {}: '.format(lower, upper)))


if __name__ == '__main__':
    main()
