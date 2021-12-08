import sys

filename = 'days/7/input.txt'


def get_input():
    with open(filename) as file:
        return [int(number) for number in file.readline().split(',')]


def task1():
    positions = get_input()
    answer = sys.maxsize

    for alignment in range(max(positions)):
        fuel_used = 0

        for crab in positions:
            fuel_used += abs(crab - alignment)

        if fuel_used < answer:
            answer = fuel_used

    print("\tAnswer: ", answer)


def task2():
    positions = get_input()
    answer = sys.maxsize

    for alignment in range(max(positions)):
        fuel_used = 0

        for crab in positions:
            fuel_used += sum(range(1, abs(crab - alignment) + 1))

        if fuel_used < answer:
            answer = fuel_used

    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
