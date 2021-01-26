from brain_games.games import game_even, game_calc,\
    game_gcd, game_progression, game_prime
from brain_games.cli import welcome_user
import prompt


def status(*args):
    name = welcome_user()
    print('Hello, {}!'.format(name))
    game = args[0]
    i = 0
    not_correct = "'{}' is wrong answer; (. Correct answer was '{}'."
    condition = get_description(game)
    print(condition)
    while i <= 3:
        suite = list(game.get_question_answer())
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


def get_description(game):
    description = {
        game_even:
            'Answer "yes" if the number is even, otherwise answer "no".',
        game_calc:
            'What is the result of the expression?',
        game_gcd:
            'Find the greatest common divisor of given numbers.',
        game_progression:
            'What number is missing in the progression?',
        game_prime:
            'Answer "yes" if given number is prime. Otherwise answer "no".'
    }
    return description[game]
