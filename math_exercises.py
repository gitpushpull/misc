from enum import Enum
from datetime import datetime
from random import randint, seed
from math import isclose


class Opr(Enum):
    ADD = '+'
    SUB = '-'
    MUL = 'x'
    DIV = u'\u00F7'

CHOICE_OPS = [None, Opr.ADD, Opr.SUB, Opr.MUL, Opr.DIV]
CHOICE_DIF = [None, 10, 20, 50, 100]

def get_nums(range_start, range_end, opr):
    num1 = randint(range_start, range_end)
    range_end = num1 if opr == Opr.SUB or opr == Opr.DIV else range_end
    num2 = randint(range_start, range_end)
    return num1, num2

def get_answer(num1, num2, opr):
    ans = 'q'
    try:
        ans = input('{0} {2} {1} = '.format(num1, num2, opr.value)).lower()
        if ans != 'q':
            ans = float(ans) if opr == Opr.DIV else int(ans)
    except:
        print('Invalid input. Please try again.')
        return get_answer(num1, num2, opr)
    return ans

def check_answer(num1, num2, ans, opr):
    if (opr == Opr.ADD):
        return num1 + num2 == ans
    elif (opr == Opr.SUB):
        return num1 - num2 == ans
    elif (opr == Opr.MUL):
        return num1 * num2 == ans
    elif (opr == Opr.DIV):
        return isclose(round(num1 / num2, 2), round(ans, 2))

    return False

def get_choice(prompt, start_range, end_range):
    choice = -1

    while not (start_range <= choice <= end_range):
        try:
            choice = int(input(prompt))
        except:
            print('Invalid input, please try again.')

    return choice

def get_exercise():
    choice_prompt = 'Please chose what you want to practice:\n1: Addition\n'\
    '2: Subtraction\n3: Multiplication\n4: Division\n'

    return get_choice(choice_prompt, 1, 4)

def get_difficulty():
    choice_prompt = 'Please select difficulty level:\n1: Easy\n'\
    '2: Normal\n3: Hard\n4: Extreme\n'

    return get_choice(choice_prompt, 1, 4)


def main():
    print('Q to quit.')
    choice = get_exercise()
    opr = CHOICE_OPS[choice]
    choice = get_difficulty()
    range_start = 1
    range_end = CHOICE_DIF[choice]
    stop = False
    while not stop:
        num1, num2 = get_nums(range_start, range_end, opr)
        ans = get_answer(num1, num2, opr)
        if ans == 'q':
            stop = True
        while not stop and not check_answer(num1, num2, ans, opr):
            print('Wrong answer, try again: ')
            ans = get_answer(num1, num2, opr)
            if ans == 'q':
                stop = True
        if not stop:
            print('Great job.')

main()

