from collections import defaultdict
from itertools import product

import functions

filename = 'days/11/input.txt'


def task1():
    _input = functions.read_file_to_list(filename, str)

    octopuses = defaultdict(int)

    for r in range(10):
        for c in range(10):
            octopuses[(r, c)] = int(_input[r][c])

    answer = 0

    for step in range(100):
        original_flashed = set()

        for point, value in octopuses.items():
            octopuses[point] = value + 1

            if octopuses[point] > 9:
                octopuses[point] = 0
                original_flashed.add(point)

        complete = original_flashed.copy()

        while len(original_flashed) > 0:
            p = original_flashed.pop()
            flash(p, complete, octopuses)

        answer += len(complete)

    print("\tAnswer: ", answer)


def flash(point, flashed, octopuses):
    x, y = point

    x1 = max(0, x - 1)
    x2 = min(10, x + 2)
    y1 = max(0, y - 1)
    y2 = min(10, y + 2)

    # points to compare
    points = product(range(x1, x2), range(y1, y2))

    for p in points:
        # ignore self and flashed
        if p != point and p not in flashed:
            octopuses[p] += 1

            if octopuses[p] > 9:
                flashed.add(p)
                octopuses[p] = 0
                flash(p, flashed, octopuses)


def task2():
    _input = functions.read_file_to_list(filename, str)

    octopuses = defaultdict(int)

    for r in range(10):
        for c in range(10):
            octopuses[(r, c)] = int(_input[r][c])

    answer = 0
    all_flashed = False
    while not all_flashed:
        answer += 1
        original_flashed = set()

        for point, value in octopuses.items():
            octopuses[point] = value + 1

            if octopuses[point] > 9:
                octopuses[point] = 0
                original_flashed.add(point)

        complete = original_flashed.copy()

        while len(original_flashed) > 0:
            p = original_flashed.pop()
            flash(p, complete, octopuses)

        if len(complete) == 100:
            all_flashed = True

    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
