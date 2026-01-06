import numpy as np
from functools import reduce
from itertools import combinations

from scipy.optimize import linprog

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _get_min_no_of_presses(line):
    goal, *buttons, _ = line.strip().split(" ")
    goal = goal.strip('[]').replace('.', '0').replace('#', '1')
    no_of_bits = len(goal)
    buttons = [
        sum(2**(no_of_bits - i - 1) for i in map(int, b.strip("()").split(",")))
        for b in buttons
    ]
    goal = int(goal, 2)

    for no_of_presses in range(1, len(buttons)):
        for pressed_buttons in combinations(buttons, no_of_presses):
            if reduce(lambda x, y: x ^ y, pressed_buttons) == goal:
                return no_of_presses


@register_solution(2025, 10, 1)
def part_one(input_file_path: str):
    return sum(_get_min_no_of_presses(line) for line in yield_lines(input_file_path))


@register_solution(2025, 10, 2)
def part_two(input_file_path: str):
    total = 0
    for line in yield_lines(input_file_path):
        _, *buttons, goal = line.strip().split(" ")
        goal = list(map(int, goal.strip('{}').split(',')))
        buttons = tuple(tuple(map(int, b.strip("()").split(","))) for b in buttons)
        goal_length = len(goal)

        A = np.transpose(np.array([[1 if i in b else 0 for i in range(goal_length)] for b in buttons]))
        c = len(A[0]) * [1]

        for method in ["highs", "highs-ds", "highs-ipm", "interior-point", "revised simplex", "simplex"]:
            result = linprog(c=c, A_eq=A, b_eq=goal, method=method, integrality=1)
            
            if goal == (list(sum(a) for a in zip(*[[int(c) if i in b else 0 for i in range(goal_length)] for b, c in zip(buttons, result.x)]))):
                total += sum(map(int, result.x))
                break

    return total


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 10)
    part_one(input_file_path)
    part_two(input_file_path)
