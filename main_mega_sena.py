from time import sleep

from funcs_mega_sena import (choose_one_number, chosen_numbers,
                             total_rightness, validate_int, value_game,
                             winners, winning, winning_numbers)

#  Price for each game
for key, value in value_game().items():
    print(f'{key} numbers - Price: R${value}')

#  Define how many numbers being gamble
gamble = input('\nWrite how many number you like gamble: ')
total_numbers = validate_int(gamble)

if total_numbers < 6 or total_numbers > 15:
    raise ValueError('You need choose numbers between 6 and 15!')


#  Define Numbers the user choose
number = choose_one_number(total_numbers)

print('Your numbers: ', end='')
for choice in sorted(chosen_numbers):
    print(choice, end=' ')


#  Define corrects numbers
print('\nWinning Numbers: ', end='')
winning_numbers()
for value in sorted(winners):
    print(value, end=' ')
    sleep(2)

print(f'\n{total_rightness()}\n{winning()}')
