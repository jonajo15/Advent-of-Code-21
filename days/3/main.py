filename = 'input.txt'


def read_file_to_list(_type):
    with open(filename) as file:
        return [_type(line.rstrip()) for line in file.readlines()]


def task1():
    data = read_file_to_list(str)
    gamma = ''

    for i in range(len(data[0])):
        gamma += get_most_common(data, i)

    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

    g_rate = int(gamma, 2)
    e_rate = int(epsilon, 2)

    answer = g_rate * e_rate
    print("\tAnswer: ", answer)


def get_most_common(lst, i):
    sum_col = 0

    for d in lst:
        sum_col += int(d[i])

    return '1' if sum_col >= len(lst) / 2 else '0'


def get_least_common(lst, i):
    sum_col = 0

    for d in lst:
        sum_col += int(d[i])

    return '0' if sum_col >= len(lst) / 2 else '1'


def task2():
    data = read_file_to_list(str)

    oxy_filter = data
    co2_filter = data

    for i in range(len(data[0])):
        oxy_val = get_most_common(oxy_filter, i)
        co2_val = get_least_common(co2_filter, i)

        if len(oxy_filter) > 1:
            oxy_filter = list(filter(lambda d: d[i] == oxy_val, oxy_filter))

        if len(co2_filter) > 1:
            co2_filter = list(filter(lambda d: d[i] == co2_val, co2_filter))

    oxy_rate = int(oxy_filter[0], 2)
    co2_rate = int(co2_filter[0], 2)

    answer = oxy_rate * co2_rate
    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
