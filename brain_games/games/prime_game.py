from .engine import (
    welcome_user,
    game_rule,
    question,
    answer_check,
    answer_request_string,
    random_number_generation,
    congratulations,
)


def is_prime(n):
    if n == 1:
        return 'no'
    if n == 2:
        return 'yes'
    i = 2
    while i < n:
        if n % i == 0:
            return 'no'
        i += 1
    return 'yes'


def prime_brain_game():
    usernames = []
    answers = []
    correct_answers = []
    numbers = []
    even_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    welcome_user(usernames)
    game_rule(even_rule)
    n = 0
    while n < 3:
        answers = []
        random_number_generation(numbers)
        number = numbers.pop()
        prime_question = f'{str(number)}'
        question(prime_question)
        correct_answer = is_prime(number)
        correct_answers.append(correct_answer)
        answer_request_string(answers)
        answer_check(answers, correct_answers, usernames)
        if usernames == []:
            return
        n += 1
    congratulations(usernames)
    return
