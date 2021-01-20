#!/usr/bin/env python3
from random import randint, choice
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def status(*args):
    args = args[0]
    answer = args[1]
    question = args[0]
    # print(answer)
    b = "'{}' is wrong answer; (. Correct answer was '{}'."
    print('Question: {}'.format(question))
    if type(answer) is int:
        user_answer = prompt.integer('Your answer: ')
        if user_answer == answer:
            print("Correct!")
            return True
        else:
            return print(b.format(user_answer, answer))
    else:
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print("Correct!")
            return True
        else:
            return print(b.format(user_answer, answer))


def question_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    char = '+-*'
    operation = choice(char)
    question = '{} {} {}'.format(num_1, operation, num_2)
    answer_even = 'yes' if num_1 % 2 == 0 else 'no'
    answer_calc = eval(question)
    return question, answer_calc, num_1, answer_even


if __name__ == '__main__':
    welcome_user()
    status()
    question_answer()
