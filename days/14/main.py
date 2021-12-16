from collections import defaultdict

import functions

filename = 'days/14/input.txt'


def task1():
    _input = functions.read_file_to_list(filename, str)
    line_break_index = _input.index('')

    template = _input[:line_break_index][0]
    insertions = dict(r.split(' -> ') for r in _input[line_break_index+1:])

    polymer = defaultdict(int)

    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        polymer[pair] += 1

    for step in range(40):
        temp_polymer = defaultdict(int)

        for poly in polymer.keys():
            value = insertions[poly]
            key1 = poly[0] + value
            key2 = value + poly[1]

            temp_polymer[key1] += polymer[poly]
            temp_polymer[key2] += polymer[poly]

        polymer = temp_polymer

    letters = defaultdict(int)

    # add first letter
    letters[template[0]] += 1

    for poly, value in polymer.items():
        letters[poly[1]] += value

    most_common = max(letters, key=letters.get)
    least_common = min(letters, key=letters.get)

    answer = letters[most_common] - letters[least_common]

    print("\tAnswer: ", answer)


def task2():
    _input = functions.read_file_to_list(filename, str)

    answer = 0

    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
