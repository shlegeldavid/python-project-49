import prompt
import random


def is_even(n):
    if n % 2 == 0:
        return 'yes'
    return 'no'


def main():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    while n < 3:
        random_number = random.randint(1, 100)
        print('Question: ' + str(random_number))
        answer = prompt.string('Your answer: ')
        if is_even(random_number) == answer:
            print('Correct!')
            n += 1
        else:
            if answer == 'yes':
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
