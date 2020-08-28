#!/usr/bin/env python3

from random import randint

# TODO
# fix shifting letters (or whatever else that causes random changes in output)

incomp_factor = int(input('Incomprehensibility factor (0 - 100%): '))
output_string = ''

angry_mode = input('Angry mode (Y/n): ')
angry_mode = False if angry_mode.lower() == 'n' else True
angry_percent = 0.1
angry_string = ''

input_string = input('Input string: ')

shifted = False

for i in range(len(input_string)):
    if randint(0, 100) > incomp_factor:
        output_string += input_string[i]
        continue

    choices = {'case switch': [i for i in range(1, 1 + 15)]}
    choices['delete letter'] = [i for i in range(choices['case switch'][-1] + 2)]
    choices['shift letters'] = [i for i in range(choices['delete letter'][-1] + 28)]
    choices['miss-click'] = [i for i in range(choices['shift letters'][-1] + 55)]

    choice = randint(1, choices['miss-click'][-1])

    if choice in choices['shift letters'] or shifted is not False:
        if shifted is not False:
            output_string += shifted
            shifted = False
        else:
            try:
                output_string += input_string[i + 1]
            except IndexError:
                output_string += input_string[i]

            shifted = input_string[i]
        continue

    elif choice in choices['case switch']:
        output_string += input_string[i].upper() if input_string[i] == input_string[i].lower() \
            else input_string[i].lower()

    elif choice in choices['delete letter']:
        continue

    elif choice in choices['miss-click']:
        miss_clicked = {'q': 'aw',
                        'w': 'qes',
                        'e': 'wrd',
                        'r': 'etf',
                        't': 'ryg',
                        'y': 'tuh',
                        'u': 'yij',
                        'i': 'uok',
                        'o': 'ipl',
                        'p': 'o[;-',
                        'a': 'zsq',
                        's': 'adxw',
                        'd': 'sfrec',
                        'f': 'dgvr',
                        'g': 'fhtb',
                        'h': 'gjyn',
                        'j': 'hkum',
                        'k': 'jl,i',
                        'l': 'k;o.',
                        'z': 'asx',
                        'x': 'sdzc',
                        'c': 'xvdf ',
                        'v': 'cbfg ',
                        'b': 'vngh ',
                        'n': 'bmhj ',
                        'm': 'n,jk ',
                        ',': 'm,.kl',
                        '.': ',./l;',
                        '!': '1'}
        try:
            output_string += miss_clicked[input_string[i]][randint(0, len(miss_clicked[input_string[i]]) - 1)]
        except KeyError:
            output_string += input_string[i]

if angry_mode:
    for word in output_string.split(sep=' '):
        if randint(1, 100) <= angry_percent * 100:
            angry_string += word.upper()
        else:
            angry_string += word
        angry_string += ' '

print(output_string) if angry_mode is False else print(angry_string)
# input()
