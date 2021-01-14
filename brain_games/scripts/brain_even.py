#!/usr/bin/env python3
import random
import prompt
from brain_games import cli


def main():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index <= 3:
        num = random.randint(1, 100)
        print('Question: {}'.format(num))
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        if num % 2 == 0 and answer == 'yes' or num % 2 != 0 and answer == 'no':
            print("Correct!")
            index = index + 1
            if index == 3:
                return print("Congratulations, {}!".format(name))
        else:
            print(
                "'{}' is wrong answer; (."
                " Correct answer was '{}'.".format(answer, correct_answer))
            break


if __name__ == '__main__':
    main()
