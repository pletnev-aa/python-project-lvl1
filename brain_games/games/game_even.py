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
    answer = 'yes' if num_1 % 2 == 0 else 'no'
    question = num_1
    return question, answer
