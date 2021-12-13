from collections import defaultdict

import functions

filename = 'input.txt'


def task1():
    _input = functions.read_file_to_list(filename, str)
    newline_index = _input.index('')
    coords = _input[:newline_index]
    folds = _input[newline_index + 1:]
    folded_map = set()

    for coord in coords:
        x, y = coord.split(',')
        point = (int(x), int(y))

        folded_map.add(point)

    f_dir, f_mag = folds[0].split(' ')[-1].split('=')
    temp_folded_map = set()

    for point in folded_map:
        if f_dir == 'y':
            if point[1] > int(f_mag):
                new_y = int(f_mag) - (point[1] - int(f_mag))

                temp_folded_map.add((point[0], new_y))
            else:
                temp_folded_map.add(point)
        if f_dir == 'x':
            if int(point[0]) > int(f_mag):
                new_x = int(f_mag) - (point[0] - int(f_mag))

                temp_folded_map.add((new_x, point[1]))
            else:
                temp_folded_map.add(point)

        folded_map = temp_folded_map

    answer = len(folded_map)

    print("\tAnswer: ", answer)


def task2():
    _input = functions.read_file_to_list(filename, str)
    newline_index = _input.index('')
    coords = _input[:newline_index]
    folds = _input[newline_index + 1:]
    folded_map = set()

    for coord in coords:
        x, y = coord.split(',')
        point = (int(x), int(y))

        folded_map.add(point)

    for fold in folds:
        f_dir, f_mag = fold.split(' ')[-1].split('=')
        temp_folded_map = set()

        for point in folded_map:
            if f_dir == 'y':
                if point[1] > int(f_mag):
                    new_y = int(f_mag) - (point[1] - int(f_mag))

                    temp_folded_map.add((point[0], new_y))
                else:
                    temp_folded_map.add(point)
            if f_dir == 'x':
                if int(point[0]) > int(f_mag):
                    new_x = int(f_mag) - (point[0] - int(f_mag))

                    temp_folded_map.add((new_x, point[1]))
                else:
                    temp_folded_map.add(point)

            folded_map = temp_folded_map

    print_map(folded_map)


def print_map(folded_map):
    max_x = max(list(map(lambda p: p[0], folded_map)))
    max_y = max(list(map(lambda p: p[1], folded_map)))

    for y in range(max_y + 1):
        line = ''
        for x in range(max_x + 1):
            if (x, y) in folded_map:
                line += '#'
            else:
                line += '.'
        print(line)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
