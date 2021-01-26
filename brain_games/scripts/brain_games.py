#!/usr/bin/env python3
from brain_games import cli


def main():
    name = cli.welcome_user()
    return print('Hello, {}!'.format(name))


if __name__ == '__main__':
    main()
