from collections import defaultdict

filename = 'input.txt'


def get_input():
    with open(filename) as file:
        return [int(number) for number in file.readline().split(',')]


def get_fish(days):
    timers = get_input()
    fish = defaultdict(int)

    for t in timers:
        fish[t] += 1

    for day in range(days):
        temp_fish = defaultdict(int)

        for timer, count in fish.items():
            if timer == 0:
                temp_fish[8] += count
                temp_fish[6] += count
            else:
                temp_fish[timer - 1] += count

        fish = temp_fish

    return sum(fish.values())


def task1():
    answer = get_fish(80)

    print("\tAnswer: ", answer)


def task2():
    answer = get_fish(256)

    print("\tAnswer: ", answer)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
