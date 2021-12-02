import functions

filename = 'input.txt'


def task1():
    moves = functions.read_file_to_list(filename, str)
    position = [0, 0]

    for move in moves:
        direction, amount = move.split(' ')
        if direction == 'forward':
            position[0] += int(amount)
        if direction == 'up':
            position[1] -= int(amount)
        if direction == 'down':
            position[1] += int(amount)

    answer = position[0] * position[1]
    print("\tAnswer: ", answer)


def task2():
    moves = functions.read_file_to_list(filename, str)
    position = [0, 0, 0]

    for move in moves:
        direction, amount = move.split(' ')
        if direction == 'forward':
            position[0] += int(amount)
            position[1] += int(amount) * position[2]
        if direction == 'up':
            position[2] -= int(amount)
        if direction == 'down':
            position[2] += int(amount)

    answer = position[0] * position[1]
    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
