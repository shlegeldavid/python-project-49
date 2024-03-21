from .engine import (
    welcome_user,
    game_rule,
    question,
    answer_check,
    answer_request_string,
    random_number_generation,
    congratulations,
)


def is_even(n):
    if n % 2 == 0:
        return 'yes'
    return 'no'


def even_brain_game():
    usernames = []
    answers = []
    correct_answers = []
    numbers = []
    even_rule = 'Answer "yes" if the number is even, otherwise answer "no".'

    welcome_user(usernames)
    game_rule(even_rule)
    n = 0
    while n < 3:
        answers = []
        random_number_generation(numbers)
        number = numbers.pop()
        even_question = f'{str(number)}'
        question(even_question)
        correct_answer = is_even(number)
        correct_answers.append(correct_answer)
        answer_request_string(answers)
        answer_check(answers, correct_answers, usernames)
        if usernames == []:
            return
        n += 1
    congratulations(usernames)
    return
