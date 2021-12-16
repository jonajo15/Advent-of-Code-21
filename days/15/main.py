from collections import defaultdict

import functions

filename = 'days/15/input.txt'


def task1():
    _input = functions.read_file_to_list(filename, str)

    width = len(_input[0])
    height = len(_input)

    _map = dict()
    for r in range(height):
        for c in range(width):
            _map[(r, c)] = int(_input[r][c])

    end = (height - 1, width - 1)

    answer = find_shortest_path(_map, end)

    print("\tAnswer: ", answer)


# semi-dijkstra
def find_shortest_path(_map, end):
    start = (0, 0)
    risks = {
        start: 0
    }
    queue = [start]

    while queue:
        position = queue.pop(0)
        x, y = position
        risk = risks.get(position)

        # iterate valid neighbors
        neighbors = list(filter(lambda p: p in _map, [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]))
        for nb in neighbors:
            old_risk = risks.get(nb, None)
            new_risk = risk + _map[nb]

            # if unexplored or lower risk
            if not old_risk or new_risk < old_risk:
                risks[nb] = new_risk
                queue.append(nb)

    return risks[end]


def task2():
    _input = functions.read_file_to_list(filename, str)

    height = len(_input[0])
    width = len(_input)

    _map = dict()
    for r in range(height):
        for c in range(width):
            _map[(r, c)] = int(_input[r][c])

    # expand down
    full_map = _map.copy()
    for point, risk in _map.items():
        x, y = point
        for i in range(1, 5):
            mod_risk = (risk + i) % 9
            new_risk = 9 if mod_risk == 0 else mod_risk

            new_x = x + (height * i)
            full_map[(new_x, y)] = new_risk

    # expand right
    _map = full_map.copy()
    for point, risk in _map.items():
        x, y = point
        for i in range(1, 5):
            mod_risk = (risk + i) % 9
            new_risk = 9 if mod_risk == 0 else mod_risk

            new_y = y + (width * i)
            full_map[(x, new_y)] = new_risk

    end = (height * 5 - 1, width * 5 - 1)

    answer = find_shortest_path(full_map, end)

    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
