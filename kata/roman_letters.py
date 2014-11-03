__author__ = 'manu'

steps = [0, 5, 10, 50, 100, 500, 1000]


def to_roman(number):
    isolated_numbers = get_isolated_numbers(number)
    roman = ""
    for isolated_number in isolated_numbers:
        roman += get_isolated_roman(isolated_number)
    return roman


def get_isolated_numbers(number):
    isolated_numbers = []
    str_number = str(number)
    nb_digits = len(str_number)
    for i in range(0, nb_digits):
        if len(isolated_numbers) != 0:
            for j in range(0, len(isolated_numbers)):
                isolated_numbers[j] *= 10

        if str_number[i] != '0':
            isolated_numbers.append(int(str_number[i]))
    return isolated_numbers


def get_isolated_roman(number):
    step = get_current_step(number)
    position = get_number_position_in_step(number)
    simple_char = get_roman_char(step)
    start_with_5 = is_start_with_5(steps[step])
    roman = ""

    if step == 6 and position == 4:
        return "MMMM"

    if not start_with_5:
        if position == 4:
            roman = simple_char + get_roman_char(step + 1)
        elif position < 4:
            for i in range(0, position):
                roman += simple_char
    else:
        char_before = get_roman_char(step - 1)
        if position == 0:
            return simple_char
        elif position == 4:
            roman = char_before + get_roman_char(step + 1)
        elif position < 4:
            roman = simple_char
            for i in range(0, position):
                roman += char_before
    return roman


def is_start_with_5(number):
    return str(number).startswith("5")


def get_roman_char(step):
    steps_roman = ["I", "V", "X", "L", "C", "D", "M"]
    return steps_roman[step]


def get_number_position_in_step(number):
    if number < 5:
        return number
    elif number < 10:
        return number - 5
    elif number < 50:
        return number / 10
    elif number < 100:
        return (number - 50) / 10
    elif number < 500:
        return number / 100
    elif number < 1000:
        return (number - 500) / 100
    else:
        return number / 1000


def get_current_step(number):
    for step in steps:
        i = steps.index(step)
        if step > number:
            return i - 1
        elif step == number:
            return i
    return len(steps) - 1