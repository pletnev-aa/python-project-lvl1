#!/usr/bin/env python3
from brain_games import engine
from random import randint, choice


def run(game):
    status = engine.status(game)
    if status:
        name = status[1]
        return print("Congratulations, {}!".format(name))


def get_question_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    operation = choice('+-*')
    question = '{} {} {}'.format(num_1, operation, num_2)
    answer = eval(question)
    return question, answer
