#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    return print('Hello, {}!'.format(name))


if __name__ == '__main__':
    welcome_user()
