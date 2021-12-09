import functions
from collections import defaultdict

filename = 'days/9/input.txt'


def check_adjacent(point, height_map, height, width):
    is_lowest = True
    x, y = point

    # left
    if y > 0 and height_map[point] >= height_map[(x, y - 1)]:
        is_lowest = False

    # right
    if y < width - 1 and height_map[point] >= height_map[(x, y + 1)]:
        is_lowest = False

    # up
    if x < height - 1 and height_map[point] >= height_map[(x + 1, y)]:
        is_lowest = False

    # down
    if x > 0 and height_map[point] >= height_map[(x - 1, y)]:
        is_lowest = False

    return is_lowest


def task1():
    _input = functions.read_file_to_list(filename, str)
    height_map = dict()

    for r, row in enumerate(_input):
        for col, value in enumerate(row):
            height_map[(r, col)] = int(value)

    answer = 0
    height = len(_input)
    width = len(_input[0])

    for x in range(len(_input)):
        for y in range(len(_input[0])):
            is_low_point = check_adjacent((x, y), height_map, height, width)

            if is_low_point:
                answer += height_map[(x, y)] + 1

    print("\tAnswer: ", answer)


def walk(point, height_map, height, width):
    steps = defaultdict(int)
    steps[point] = 1
    
    x, y = point

    # left
    if y > 0 and height_map[point] < height_map[(x, y - 1)] != 9:
        steps.update(walk((x, y - 1), height_map, height, width))

    # right
    if y < width - 1 and height_map[point] < height_map[(x, y + 1)] != 9:
        steps.update(walk((x, y + 1), height_map, height, width))

    # down
    if x < height - 1 and height_map[point] < height_map[(x + 1, y)] != 9:
        steps.update(walk((x + 1, y), height_map, height, width))

    # up
    if x > 0 and height_map[point] < height_map[(x - 1, y)] != 9:
        steps.update(walk((x - 1, y), height_map, height, width))

    return steps


def task2():
    _input = functions.read_file_to_list(filename, str)
    height_map = dict()

    for r, row in enumerate(_input):
        for col, value in enumerate(row):
            height_map[(r, col)] = int(value)

    height = len(_input)
    width = len(_input[0])
    basins = dict()

    for x in range(len(_input)):
        for y in range(len(_input[0])):
            is_low_point = check_adjacent((x, y), height_map, height, width)

            if is_low_point:
                basin = walk((x, y), height_map, height, width)
                basins[(x, y)] = len(basin.keys())

    answer = 1

    for value in sorted(basins.values(), reverse=True)[:3]:
        answer *= value

    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
