filename = 'input.txt'


def read_file_to_list(_type):
    with open(filename) as file:
        return [_type(line.rstrip()) for line in file.readlines()]


def read_line_by_line():
    with open(filename) as file:
        for line in file:
            print(line.rstrip())


def find(lst, key, value, _default=None):
    return next((item for item in lst if item[key] == value), _default)


def task1():
    data = read_file_to_list(int)

    count = sum((1 for i in range(1, len(data)) if data[i] - data[i - 1] > 0), 0)
    print("\tAnswer: ", count)


def task2():
    data = read_file_to_list(int)

    count = sum((1 for i in range(3, len(data)) if sum(data[i - 2:i + 1]) - sum(data[i - 3:i]) > 0), 0)
    print("\tAnswer: ", count)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
