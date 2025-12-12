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
def first_part_ai(input_file):
    dial_position = 50  # Starting position of the dial
    result = 0      # Counter for how many times the dial points at 0
    with open(input_file, 'r') as input:
        for rotation in input:
            direction = rotation[0]
            distance = int(rotation[1:])

            if direction == 'L':
                dial_position = (dial_position - distance) % 100
            elif direction == 'R':
                dial_position = (dial_position + distance) % 100

            # Check if the dial is pointing at 0 after this rotation
            if dial_position == 0:
                result += 1

    return result

@AoC.timer
def second_part(input_file):
    # Create a deque
    dial = deque([i for i in range(100)])
    result = 0
    dial.rotate(50) # Start at position 50
    with open(input_file, 'r') as input:
        for line in input:
            letter = line[0]
            number = int(line[1:])
            result += number//100
            remainder = number % 100
            if letter == 'R':
                if dial[0] != 0 and dial[0] + remainder > 100:
                    result += 1
                dial.rotate(-remainder)
            elif letter == 'L':
                if dial[0] != 0 and dial[0] - remainder < 0:
                    result += 1
                dial.rotate(remainder)
            if dial[0] == 0:
                result += 1
    return result

@AoC.timer
def second_part_ai(input_file):
    dial_position = 50  # Starting position
    zero_count = 0      # Total count of times dial points at 0
    with open(input_file, 'r') as input:
        for rotation in input:
            direction = rotation[0]
            distance = int(rotation[1:])

            # Simulate each click during the rotation
            if direction == 'L':
                # Moving left: decreasing position
                for _ in range(distance):
                    dial_position = (dial_position - 1) % 100
                    if dial_position == 0:
                        zero_count += 1
            elif direction == 'R':
                # Moving right: increasing position
                for _ in range(distance):
                    dial_position = (dial_position + 1) % 100
                    if dial_position == 0:
                        zero_count += 1

    return zero_count


if __name__ == '__main__':
    DAY = '01'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('input/input'+DAY+'.txt')))
    print('First AI solution for day' + DAY + ': ')
    print('Result: ' + str(first_part_ai('input/input'+DAY+'.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('input/input'+DAY+'.txt')))
    print('Second AI solution for day' + DAY + ': ')
    print('Result: ' + str(second_part_ai('input/input'+DAY+'.txt')))