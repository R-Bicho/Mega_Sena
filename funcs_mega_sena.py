import re
from random import randint

winners: list[int] = []
chosen_numbers: list[str] = []
total_prize = 20
right_choice: set[int] = set()
numbers_reg_exp = re.compile(r'^[1-60]$')


def winning_numbers() -> None:
    '''Define winning numbers in mega sena'''

    not_duplicate: set[int] = set()
    while len(not_duplicate) != 6:
        not_duplicate.add(randint(1, 60))

    for number in not_duplicate:
        winners.append(number)


def choose_one_number(number: int):
    '''defines the numbers chosen by the users'''

    not_duplicate: set[str] = set()
    while len(not_duplicate) != number:
        decision = input('Choose one number: ')
        not_duplicate.add(decision)

    for value in not_duplicate:
        chosen_numbers.append(value)


def validate_int(value):
    '''validates if the number is integer'''

    if numbers_reg_exp.match(value):
        value = int(value)
    else:
        print('You need write only values!')
