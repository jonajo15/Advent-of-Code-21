def read_file_to_list(filename, _type):
    with open(filename) as file:
        return [_type(line.rstrip()) for line in file.readlines()]


def read_line_by_line(filename):
    with open(filename) as file:
        for line in file:
            print(line.rstrip())


def find(lst, key, value, _default=None):
    return next((item for item in lst if item[key] == value), _default)