__author__ = 'manu'


def to_roman(number):
    roman_start = ["", "V"]
    current_step = get_current_step(number)
    roman = roman_start[current_step]

    for i in range(0, number):
        roman += "I"
        if len(roman) == 4:
            roman = "I" + roman_start[current_step+1]
    return roman

def get_current_step(number):
    steps = [0, 5]
    return 0