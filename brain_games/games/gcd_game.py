from .engine import (
    gcd_func,
    welcome_user,
    game_rule,
    question,
    answer_check,
    answer_request_integer,
    random_number_generation,
    congratulations
)


def gcd_brain_game():
    usernames = []
    answers = []
    correct_answers = []
    numbers = []
    gcd_rule = 'Find the greatest common divisor of given numbers.'

    welcome_user(usernames)
    game_rule(gcd_rule)
    n = 0
    while n < 3:
        answers = []
        random_number_generation(numbers)
        random_number_generation(numbers)
        first_number = numbers.pop(0)
        second_number = numbers.pop()
        gcd_question = f'{str(first_number)} {str(second_number)}'
        question(gcd_question)
        gcd = gcd_func(first_number, second_number)
        correct_answers.append(gcd)
        answer_request_integer(answers)
        answer_check(answers, correct_answers, usernames)
        if usernames == []:
            return
        n += 1
    congratulations(usernames)
    return
