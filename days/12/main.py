from collections import defaultdict

import functions

filename = 'days/12/input.txt'


def task1():
    _input = functions.read_file_to_list(filename, str)

    connections = dict()

    for conn in _input:
        right, left = conn.split('-')

        if right not in connections:
            connections[right] = set()
        if left not in connections:
            connections[left] = set()

        connections[right].add(left)
        connections[left].add(right)

    paths = set()

    current_path = []
    for cave in connections['start']:
        current_path.append(('start', cave))

    while current_path:
        path = current_path.pop()
        *caves, from_cave = path

        for next_cave in connections[from_cave]:

            # no revisit small caves
            if next_cave.islower() and next_cave in path:
                continue

            new_path = path + (next_cave, )

            if next_cave == 'end' and new_path not in paths:
                paths.add(new_path)
                continue

            current_path.append(new_path)

    answer = len(paths)

    print("\tAnswer: ", answer)


def check_occurences(caves):
    occ = dict()
    once = False

    for cave in caves:
        if cave.islower():
            if cave in occ:
                if not once:
                    once = True
                else:
                    return True
            else:
                occ[cave] = 1

    return False


# very slow :/
def task2():
    _input = functions.read_file_to_list(filename, str)

    connections = dict()

    for conn in _input:
        right, left = conn.split('-')

        if right not in connections:
            connections[right] = set()
        if left not in connections:
            connections[left] = set()

        connections[right].add(left)
        connections[left].add(right)

    paths = set()

    current_path = []
    for cave in connections['start']:
        current_path.append(('start', cave))

    while current_path:
        path = current_path.pop()
        *caves, from_cave = path

        occured = check_occurences(path)

        for next_cave in connections[from_cave]:

            # only visit start once and one small cave twice
            if next_cave == 'start' or (next_cave.islower() and occured):
                continue

            new_path = path + (next_cave,)

            if next_cave == 'end' and new_path not in paths:
                paths.add(new_path)
                continue

            current_path.append(new_path)

    answer = len(paths)

    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
