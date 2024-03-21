from .engine import (
    welcome_user,
    game_rule,
    question,
    answer_check,
    answer_request_integer,
    random_number_for_progression,
    congratulations,
    random
)


def numbers_to_list(i, number, progression_value, numbers):
    while i < random.randint(5, 10):
        number += progression_value
        numbers.append(number)
        i += 1


def progression_brain_game():
    usernames = []
    answers = []
    correct_answers = []
    progression_rule = 'What number is missing in the progression?'

    welcome_user(usernames)
    game_rule(progression_rule)
    n = 0
    while n < 3:
        number_progression = ''
        i = 0
        index = 0
        answers = []
        numbers = []
        random_number_for_progression(numbers)
        number = numbers.pop()
        progression_value = random.randint(2, 13)
        numbers_to_list(i, number, progression_value, numbers)
        list_length = len(numbers)
        missing_part = random.choice(numbers)
        for i in range(list_length):
            if numbers[i] == missing_part:
                numbers[i] = '..'
        while index < list_length:
            number = numbers.pop(0)
            number_progression = number_progression + str(number) + ' '
            index += 1
        correct_answers.append(missing_part)
        question(number_progression)
        answer_request_integer(answers)
        answer_check(answers, correct_answers, usernames)
        if usernames == []:
            return
        n += 1
    congratulations(usernames)
    return
