import re
from random import randint

winners: list[int] = []
chosen_numbers: list[str] = []
total_prize = 20
rightness: set[int] = set()
numbers_reg_exp = re.compile(r'^\b([1-9]|[1-5][0-9]|60)\b$')


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
        validate_int(decision)
        not_duplicate.add(decision)

    for value in not_duplicate:
        chosen_numbers.append(value)


def validate_int(value):
    '''validates if the number is integer'''

    if numbers_reg_exp.match(value):
        return int(value)
    else:
        raise ValueError('Invalid Number!')


def value_game() -> dict:
    '''Price for each game'''

    prices = {'6': '4,50', '7': '31.50', '8': '126,00', '9': '378,00',
              '10': '945,00', '11': '2.079,00', '12': '4.158,00',
              '13': '7.722,00', '14': '13.513,50', '15': '22.522,50'}
    return prices


def winning():
    '''Award for rightness'''

    six_acerts = total_prize * 0.35
    five_acerts = total_prize * 0.19
    four_acerts = total_prize * 0.19

    if len(rightness) <= 3:
        return 'You lose'

    if len(rightness) == 4:
        return f'You winnig: R${four_acerts:.2f}'

    if len(rightness) == 5:
        return f'You winnig: R${five_acerts:.2f}'

    if len(rightness) == 6:
        return f'You winnig: R${six_acerts:.2f}'


def total_rightness():
    '''writes to the user total hits'''

    for gamble in chosen_numbers:
        gamble = int(gamble)
        if gamble in winners:
            rightness.add(gamble)

    if len(rightness) <= 3:
        return f'You hit {len(rightness)} numbers'

    if len(rightness) == 4:
        return 'You hit 4 numbers'

    if len(rightness) == 5:
        return 'You hit 5 numbers'

    if len(rightness) == 6:
        return 'You hit 6 numbers'
