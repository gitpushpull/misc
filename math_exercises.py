from enum import Enum
from datetime import datetime
from random import randint, seed

class Opr(Enum):
    ADD = '+'
    SUB = '-'
    MUL = 'x'
    DIV = u'\u00F7'

CHOICE_OPS = [None, Opr.ADD, Opr.SUB, Opr.MUL, Opr.DIV]

def get_nums(range_start, range_end, opr):
    num1 = randint(range_start, range_end)
    num2 = randint(range_start, num1 if opr == Opr.SUB else range_end)
    return num1, num2

def get_answer(num1, num2, opr):
    ans = 'q'
    try:
        ans = input('{0} {2} {1} = '.format(num1, num2, opr.value)).lower()
        if ans != 'q':
            ans = int(ans)
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
        return num1 / num2 == ans

    return False

def get_choice():
    choice_prompt = 'Please chose what you want to practice:\n1: Addition\n'\
    '2: Subtraction\n3: Multiplication\n4: Division\n'

    choice = -1
    
    while not(1 <= choice <= 4):
        try:
            choice = int(input(choice_prompt))
        except:
            print('Invalid input, please try again.')

    return choice


def main():
    print('Q to quit.')
    choice = get_choice()
    opr = CHOICE_OPS[choice]
    range_start = 1
    range_end = 10
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

