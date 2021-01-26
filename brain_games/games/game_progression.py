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
    start = min(num_1, num_2)
    step = max(num_1, num_2) - start
    num = randint(5, 10)
    stop = start + (step * num)
    progression = list(range(start, stop, step))
    len_progression = len(progression) - 1
    hidden_num = randint(1, len_progression)
    answer = progression[hidden_num]
    progression[hidden_num] = '..'
    question = ' '.join(map(str, progression))
    return question, answer
