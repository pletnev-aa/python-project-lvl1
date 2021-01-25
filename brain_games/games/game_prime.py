#!/usr/bin/env python3
from brain_games import cli


def run(game):
    status = cli.status(game)
    if status:
        name = status[1]
        return print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    run('prime')
