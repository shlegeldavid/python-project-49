import prompt
import random

def init():
    
    usernames = []
    answers = []
    correct_answers = []
    numbers = []


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    usernames.append(name)


def game_rule(rule):
    print(rule)


def question(question_body):
    print(f'Question: {question_body}')


def answer_quest():
    answer = prompt.string('Your answer: ')
    answers.append(answer)


def wrong_answer_quest():
    print(f"'{answers.pop()}' is wrong answer ;(. Correct answer was '{correct_answers.pop()}'")
    return print(f"Let's try again, {usernames.pop}!")

def answer_check():
    if answers == correct_answers:
        print('Correct!')
    else:
        print(f"'{answers.pop()}' is wrong answer ;(. Correct answer was '{correct_answers.pop()}'")
        return print(f"Let's try again, {usernames.pop()}!")

def random_number_generation():
    random_number = random.randint(1, 100)
    numbers.append(random_number)