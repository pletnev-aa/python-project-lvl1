#!/usr/bin/env python3
# from random import randint, choice
from brain_games import cli


def run():
    name = cli.welcome_user()
    i = 0
    print('What is the result of the expression?')
    while i <= 3:
        status = cli.status(main(cli.question_answer()))
        if status:
            i = i + 1
            if i == 3:
                return print("Congratulations, {}!".format(name))
        else:
            return print("Let's try again, {}!".format(name))


def run_games():
    return


def main(*args):
    args = args[0]
    # print(args)
    question = args[0]
    answer = args[1]
    return question, answer


if __name__ == '__main__':
    main()
