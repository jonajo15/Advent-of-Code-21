filename = 'input.txt'


def read_file_to_list(_type):
    with open(filename) as file:
        return [_type(line.rstrip()) for line in file.readlines()]


def find_number_on_board(board, n):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == n:
                return i, j

    return -1, -1


def check_win(board, x, y, original):
    winner = None
    _sum = 0

    # check row
    if len(list(filter(lambda e: e is not None, board[x]))) == 5:
        winner = board

    # column
    col = [board[f][y] for f in range(len(board))]
    if len(list(filter(lambda e: e is not None, col))) == 5:
        winner = board

    if winner:
        for i in range(len(winner)):
            for j in range(len(winner[i])):
                if winner[i][j] is None:
                    _sum += original[i][j]

    return _sum


def get_boards(data):
    boards = []
    results = []
    b_index = -1

    for row in data[1:]:
        if row == '':
            b_index += 1
            boards.append([])
            results.append([])
            continue

        board_row = [int(x) for x in filter(lambda x: x != '', row.split(' '))]
        boards[b_index].append(board_row)
        results[b_index].append([None] * 5)

    return boards, results


def task1():
    data = read_file_to_list(str)
    order = [int(x) for x in data[0].split(',')]

    boards, results = get_boards(data)

    win_sum = 0
    count = 0
    number = 0

    while win_sum == 0:
        number = order[count]
        for b in range(len(boards)):
            x, y = find_number_on_board(boards[b], number)

            # number not found
            if x == y == -1:
                continue

            results[b][x][y] = number

            win_sum = check_win(results[b], x, y, boards[b])

            if win_sum > 0:
                break

        count += 1

    answer = win_sum * number

    print("\tAnswer: ", answer)


def task2():
    data = read_file_to_list(str)
    order = [int(x) for x in data[0].split(',')]

    boards, results = get_boards(data)

    last = False
    count = 0
    number = 0
    win_sum = 0
    winners = [False] * len(boards)

    while not last:
        number = order[count]
        for b in range(len(boards)):
            x, y = find_number_on_board(boards[b], number)

            # number not found
            if x == y == -1:
                continue

            results[b][x][y] = number
            win_sum = check_win(results[b], x, y, boards[b])

            if win_sum > 0:
                winners[b] = True

                # check if last winner
                if all(w is True for w in winners):
                    last = True
                    break

        count += 1

    answer = win_sum * number

    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
