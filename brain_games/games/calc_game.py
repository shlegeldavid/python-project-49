#!/usr/bin/env python3
from .engine import (
    welcome_user,
    game_rule,
    question,
    answer_check,
    answer_request_integer,
    random_number_generation,
    congratulations,
    random
)


def calc_brain_game():
    usernames = []
    answers = []
    correct_answers = []
    numbers = []
    calc_rule = 'What is the result of the expression?'
    operators = ['+', '-', '*']
    picked_operators = []

    def picked_operator():
        picked_operators.append(random.choice(operators))

    welcome_user(usernames)
    game_rule(calc_rule)
    n = 0
    while n < 3:
        answers = []
        random_number_generation(numbers)
        random_number_generation(numbers)
        picked_operator()
        first_number = numbers.pop(0)
        second_number = numbers.pop()
        picked_operator_from_coll = picked_operators.pop()
        calc_question = (str(first_number) + ' '
                         + picked_operator_from_coll + ' '
                         + str(second_number))
        question(calc_question)
        expression = 0
        match picked_operator_from_coll:
            case '+':
                expression += first_number + second_number
            case '-':
                expression += first_number - second_number
            case '*':
                expression += first_number * second_number
        correct_answers.append(expression)
        answer_request_integer(answers)
        answer_check(answers, correct_answers, usernames)
        if usernames == []:
            return
        n += 1
    congratulations(usernames)
    return
