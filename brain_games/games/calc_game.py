from .engine import *

init()
usernames = []
answers = []
correct_answers = []
numbers = []
operators = ['+', '-', '*']
picked_operators = []

def random_number_generation():
    random_number = random.randint(1, 100)
    numbers.append(random_number)

def picked_operator():
    picked_operators.append(random.choice(operators))


def calc_brain_game():
    calc_rule = 'What is the result of the expression?'
    welcome_user()
    game_rule(calc_rule)
    n = 0
    while n < 3:
        random_number_generation()
        random_number_generation()
        print(numbers)
        picked_operator()
        first_number = numbers.pop(0)
        second_number = numbers.pop()
        picked_operator_from_coll = picked_operators.pop()
        calc_question = str(first_number) + ' ' +  picked_operator_from_coll + ' ' + str(second_number)
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
        print(correct_answers)
        answer_quest()
        print(answers)
        answer_check()
        n += 1



