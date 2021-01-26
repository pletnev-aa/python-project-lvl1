#!/usr/bin/env python3
from random import randint, choice
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return name


def status(*args):
    name = welcome_user()
    print('Hello, {}!'.format(name))
    args = args[0]
    i = 0
    not_correct = "'{}' is wrong answer; (. Correct answer was '{}'."
    condition = description(args)
    print(condition)
    while i <= 3:
        suite = list(question_answer(args))
        question = suite[0]
        answer = suite[1]
        print('Question: {}'.format(question))
        if type(answer) is int:
            user_answer = prompt.integer('Your answer: ')
        else:
            user_answer = prompt.string('Your answer: ')
            user_answer = user_answer.lower()
        if user_answer == answer:
            print('Correct!')
            i = i + 1
            if i == 3:
                return True, name
        else:
            print(not_correct.format(user_answer, answer))
            return print("Let's try again, {}!".format(name))


def question_answer(game):
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    char = '+-*'
    operation = choice(char)
    if game == 'prime':
        denom = 2
        remainder = 0
        if num_1 > 1:
            while True:
                if denom * denom <= num_1 and remainder != 1:
                    if num_1 % denom == 0:
                        remainder = remainder + 1
                    denom = denom + 1
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
    elif game == 'gcd':
        question = '{} {}'.format(num_1, num_2)
        while max(num_1, num_2) % min(num_1, num_2) != 0:
            if num_1 > num_2:
                num_1 = num_1 % num_2
            elif num_1 < num_2:
                num_2 = num_2 % num_1
        answer = min(num_1, num_2)
        return question, answer
    elif game == 'progression':
        start = min(num_1, num_2)
        step = max(num_1, num_2) - start
        num = randint(5, 10)
        stop = start + (step * num)
        progression = list(range(start, stop, step))
        len_progression = len(progression) - 1
        hidden_num = randint(0, len_progression)
        answer = progression[hidden_num]
        progression[hidden_num] = '..'
        question = ' '.join(map(str, progression))
        return question, answer
    elif game == 'even':
        answer = 'yes' if num_1 % 2 == 0 else 'no'
        question = num_1
        return question, answer
    elif game == 'calc':
        question = '{} {} {}'.format(num_1, operation, num_2)
        answer = eval(question)
        return question, answer


def description(game):
    even = 'Answer "yes" if the number is even, otherwise answer "no".'
    calc = 'What is the result of the expression?'
    gcd = 'Find the greatest common divisor of given numbers.'
    progression = 'What number is missing in the progression?'
    prime = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    if game == 'even':
        return even
    elif game == 'calc':
        return calc
    elif game == 'gcd':
        return gcd
    elif game == 'progression':
        return progression
    elif game == 'prime':
        return prime


if __name__ == '__main__':
    welcome_user()
    status()
