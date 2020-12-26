#!/usr/bin/env python3
from brain_games import cli


def greet():
    print('Welcome to the Brain Games!')
    cli.welcome_user()


def main():
    greet()


if __name__ == '__main__':
    main()
