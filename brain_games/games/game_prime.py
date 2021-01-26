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
    divisor = 2
    remainder = 0
    if num_1 > 1:
        while True:
            if divisor * divisor <= num_1 and remainder != 1:
                if num_1 % divisor == 0:
                    remainder = remainder + 1
                divisor = divisor + 1
            elif remainder == 1:
                answer = 'no'
                question = num_1
                return question, answer
            else:
                answer = 'yes'
                question = num_1
                return question, answer
    else:
        answer = 'no'
        question = num_1
        return question, answer
