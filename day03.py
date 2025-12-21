import lib.AoC_lib as AoC
from collections import Counter

@AoC.timer
def first_part(input_file):
    result = 0
    with open(input_file, 'r') as input:
        for line in input:
            batteries_counter = Counter(line.strip())
            remaining_batteries = line.strip()
            highest = ''.join(sorted(remaining_batteries))[-1]
            if batteries_counter[highest] > 1:
                result += int(highest*2)
                continue
            index_highest = remaining_batteries.find(highest)
            if index_highest < len(remaining_batteries) -1:
                second_highest = ''.join(sorted(remaining_batteries[index_highest+1:]))[-1]
                result += int(highest + second_highest)
                continue
            else:
                second_highest = ''.join(sorted(remaining_batteries[:index_highest]))[-1]
                result += int(second_highest + highest)
                continue
                    
    return result


@AoC.timer
def second_part(input_file):
    result = 0
    with open(input_file, 'r') as input:
        for line in input:
            continue
                    
    return result


if __name__ == '__main__':
    DAY = '03'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))