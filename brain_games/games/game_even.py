#!/usr/bin/env python3
from brain_games import cli


def run():
    name = cli.welcome_user()
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i <= 3:
        status = cli.status(main(cli.question_answer()))
        if status:
            i = i + 1
            if i == 3:
                return print("Congratulations, {}!".format(name))
        else:
            break


def main(*args):
    args = args[0]
    # print(args)
    question = args[2]
    answer = args[3]
    return question, answer


if __name__ == '__main__':
    main()
