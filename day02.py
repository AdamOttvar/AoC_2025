import lib.AoC_lib as AoC
from collections import deque

@AoC.timer
def first_part(input_file):
    result = 0
    with open(input_file, 'r') as file:
        content = file.read().strip()
    
    sequences = content.split(',')
    for sequence in sequences:
        start, end = map(int, sequence.split('-'))
        for number in range(start, end + 1):
            len_number = len(str(number))
            if str(number)[:len_number//2] == str(number)[len_number//2:]:
                result += number

    return result


@AoC.timer
def second_part(input_file):
    result = 0
    with open(input_file, 'r') as file:
        content = file.read().strip()
    
    sequences = content.split(',')
    for sequence in sequences:
        start, end = sequence.split('-')
        for number in range(int(start), int(end) + 1):
            len_number = len(str(number))
            for idx in range(len_number//2):
                occurences = str(number).count(str(number)[:idx+1])
                if (idx+1)*occurences == len_number:
                    result += number
                    #print(f'Found matching number: {number} from pattern {str(number)[:idx+1]}')
                    break

    return result


if __name__ == '__main__':
    DAY = '02'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))