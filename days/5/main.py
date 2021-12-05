from collections import defaultdict
filename = 'input.txt'


def read_file_to_list(_type):
    with open(filename) as file:
        return [_type(line.rstrip()) for line in file.readlines()]


def task1():
    data = read_file_to_list(str)

    _map = defaultdict(int)

    for d in data:
        first, second = d.split(' -> ')
        x1, y1 = first.split(',')
        x2, y2 = second.split(',')

        y1, y2 = [int(y1), int(y2)]
        x1, x2 = [int(x1), int(x2)]

        if x1 - x2 == 0:
            for y in get_range(y1, y2):
                _map[(x1, y)] += 1
        elif y1 - y2 == 0:
            for x in get_range(x1, x2):
                _map[(x, y1)] += 1

    answer = sum(1 for p, c in _map.items() if c >= 2)

    print("\tAnswer: ", answer)


def get_range(a, b):
    if a < b:
        return range(a, b + 1)
    else:
        return range(a, b - 1, -1)


def task2():
    data = read_file_to_list(str)

    # create map
    _map = defaultdict(int)

    for d in data:
        first, second = d.split(' -> ')
        x1, y1 = first.split(',')
        x2, y2 = second.split(',')

        y1, y2 = [int(y1), int(y2)]
        x1, x2 = [int(x1), int(x2)]

        if x1 - x2 == 0:
            for y in get_range(y1, y2):
                _map[(x1, y)] += 1
        elif y1 - y2 == 0:
            for x in get_range(x1, x2):
                _map[(x, y1)] += 1
        else:
            points = zip(get_range(x1, x2), get_range(y1, y2))

            for p in points:
                _map[p] += 1

    answer = sum(1 for p, c in _map.items() if c >= 2)

    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
