#!/usr/bin/env python3
import prompt
import random


def welcome_user(usernames):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    usernames.append(name)


def game_rule(rule):
    print(rule)


def question(question_body):
    print(f'Question: {question_body}')


def answer_quest(answers):
    answer = prompt.integer('Your answer: ')
    answers.append(answer)


def answer_check(answers, correct_answers, usernames):
    answer = answers.pop()
    correct_answer = correct_answers.pop()
    if answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
        print(f"Let's try again, {usernames.pop()}!")


def random_number_generation(numbers):
    random_number = random.randint(1, 100)
    numbers.append(random_number)


def congratulations(usernames):
    name = usernames.pop()
    print(f'Congratulations, {name}!')
