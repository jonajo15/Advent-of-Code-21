def read_file_to_list(filename, _type):
    with open(filename) as file:
        return [_type(line.rstrip()) for line in file.readlines()]


def read_file_to_string(filename):
    with open(filename) as file:
        return file.read().rstrip()


def read_line_to_list(filename, _type):
    with open(filename) as file:
        return [_type(number) for number in file.readline().split(',')]


def find(lst, key, value, _default=None):
    return next((item for item in lst if item[key] == value), _default)