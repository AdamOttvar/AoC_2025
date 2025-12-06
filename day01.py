import lib.AoC_lib as AoC
from collections import deque



@AoC.timer
def first_part(input_file):
    # Create a deque
    dial = deque([i for i in range(100)])
    result = 0
    dial.rotate(50) # Start at position 50
    with open(input_file, 'r') as input:
        for line in input:
            letter = line[0]
            number = int(line[1:])
            if letter == 'R':
                dial.rotate(-number)
            elif letter == 'L':
                dial.rotate(number)
            if dial[0] == 0:
                result += 1
    return result


@AoC.timer
def second_part(input_file):
    # Create a deque
    dial = deque([i for i in range(100)])
    result = 0
    return result


if __name__ == '__main__':
    DAY = '01'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))