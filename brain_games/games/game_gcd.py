#!/usr/bin/env python3
from brain_games import engine
from random import randint


def run(game):
    status = engine.status(game)
    if status:
        name = status[1]
        return print("Congratulations, {}!".format(name))


def get_question_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = '{} {}'.format(num_1, num_2)
    while max(num_1, num_2) % min(num_1, num_2) != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        elif num_1 < num_2:
            num_2 = num_2 % num_1
    answer = min(num_1, num_2)
    return question, answer
