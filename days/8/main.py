from collections import defaultdict

filename = 'days/8/input.txt'

def read_file_to_list(filename, _type):
    with open(filename) as file:
        return [_type(line.rstrip()) for line in file.readlines()]


def task1():
    data = read_file_to_list(filename, str)

    counter = defaultdict(int)

    for d in data:
        signal_patterns, output = d.split(' | ')

        for pattern in output.split(' '):
            counter[len(pattern)] += 1

    answer = counter[2] + counter[4] + counter[3] + counter[7]

    print("\tAnswer: ", answer)


def task2():
    data = read_file_to_list(filename, str)

    answer = 0
    for d in data:
        signal_patterns, output = d.split(' | ')

        patterns = [set(p) for p in signal_patterns.split(' ')]

        def pop(f):
            p = next(p for p in patterns if f(p))
            patterns.remove(p)

            return p

        one = pop(lambda p: len(p) == 2)
        four = pop(lambda p: len(p) == 4)
        seven = pop(lambda p: len(p) == 3)
        eight = pop(lambda p: len(p) == 7)

        three = pop(lambda p: len(p) == 5 and one.issubset(p))
        nine = pop(lambda p: len(p) == 6 and three.issubset(p))
        zero = pop(lambda p: len(p) == 6 and one.issubset(p))
        six = pop(lambda p: len(p) == 6)

        six_seven = six.intersection(seven)

        five = pop(lambda p: six_seven.issubset(p))
        two = pop(lambda p: p)

        decoded = dict()
        decoded[''.join(sorted(zero))] = '0'
        decoded[''.join(sorted(one))] = '1'
        decoded[''.join(sorted(two))] = '2'
        decoded[''.join(sorted(three))] = '3'
        decoded[''.join(sorted(four))] = '4'
        decoded[''.join(sorted(five))] = '5'
        decoded[''.join(sorted(six))] = '6'
        decoded[''.join(sorted(seven))] = '7'
        decoded[''.join(sorted(eight))] = '8'
        decoded[''.join(sorted(nine))] = '9'

        value = ''
        for o in output.split(' '):
            value += decoded[''.join(sorted(o))]

        answer += int(value)

    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
