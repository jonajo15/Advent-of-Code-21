from collections import defaultdict

import functions

filename = 'input.txt'

openers = "([{<"


def task1():
    _input = functions.read_file_to_list(filename, str)

    answer = 0

    for line in _input:
        stack = list()

        for c in line:
            if c in openers:
                stack.append(c)
            else:
                combo = stack[-1] + c

                # valid
                if combo == "()" or combo == "[]" or combo == "{}" or combo == "<>":
                    stack.pop()
                else:
                    if c == ")":
                        answer += 3
                    if c == "]":
                        answer += 57
                    if c == "}":
                        answer += 1197
                    if c == ">":
                        answer += 25137
                    break

    print("\tAnswer: ", answer)


def task2():
    _input = functions.read_file_to_list(filename, str)

    answer = []

    for line in _input:
        stack = list()
        corrupted = False

        for c in line:
            if c in openers:
                stack.append(c)
            else:
                combo = stack[-1] + c

                # valid
                if combo == "()" or combo == "[]" or combo == "{}" or combo == "<>":
                    stack.pop()
                else:
                    corrupted = True
                    break

        line_score = 0
        if not corrupted:
            for c in stack[::-1]:
                line_score *= 5

                if c == '(':
                    line_score += 1
                if c == '[':
                    line_score += 2
                if c == '{':
                    line_score += 3
                if c == '<':
                    line_score += 4

            answer.append(line_score)

    median = sorted(answer)[len(answer)//2]

    print("\tAnswer: ", median)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
