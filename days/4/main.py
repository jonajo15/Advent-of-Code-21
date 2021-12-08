from dataclasses import dataclass
filename = 'days/4/input.txt'


def read_file_to_list(_type):
    with open(filename) as file:
        return [_type(line.rstrip()) for line in file.readlines()]


WIDTH = HEIGHT = 5


@dataclass
class Board:
    board: list
    marked: set

    def __init__(self, board):
        self.board = list()
        self.marked = set()

        for r in board:
            self.board += [int(v) for v in r.split(' ') if v != '']

    def find(self, number):
        try:
            index = self.board.index(number)

            return index // WIDTH, index % WIDTH
        except ValueError:
            return None

    def sum_of_rest(self):
        return sum([int(self.board[i]) for i in range(len(self.board)) if (i // WIDTH, i % WIDTH) not in self.marked])

    def set_marker(self, number):
        coord = self.find(number)

        if not coord:
            return None

        x, y = coord

        self.marked.add(coord)

        # check win
        rows = ((x, c) for c in range(WIDTH))
        cols = ((r, y) for r in range(HEIGHT))

        return all((p in self.marked) for p in rows) or all((p in self.marked) for p in cols)


def task1():
    data = read_file_to_list(str)
    order = [int(v) for v in data[0].split(',')]
    input_boards = list(filter(lambda v: v != '', data[1:]))

    boards = []
    for i in range(0, len(input_boards), 5):
        boards.append(Board(input_boards[i:i+5]))

    answer = 0

    for number in order:
        for board in boards:
            won = board.set_marker(number)

            if won:
                rest_sum = board.sum_of_rest()
                answer = rest_sum * number

                break
        else:
            continue
        break

    print("\tAnswer: ", answer)


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


# under construction
if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
