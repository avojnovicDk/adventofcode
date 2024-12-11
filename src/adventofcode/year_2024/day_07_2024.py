from itertools import product
from typing import Generator
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _is_equation_possible(result: int, operands: list[int], possible_operators: list[str]) -> bool:
    for operators in product(possible_operators, repeat=len(operands) - 1):
        expr = operands[0]
        for operand, operator in zip(operands[1:], operators):
            match operator:
                case "*" | "+":
                    expr = f"({expr}){operator}{operand}"
                case "||":
                    expr = f"int(str({expr})+'{operand}')"
        if eval(expr) == result:
            return True
    return False


def _yield_result_and_operands(input_file_path: str) -> Generator[tuple[int, list[str]], None, None]:
    for line in yield_lines(input_file_path):
        result, operands = line.split(":")
        yield (int(result), operands.split())


@register_solution(2024, 7, 1)
def part_one(input_file_path: str) -> int:
    return sum (
        result
        for result, operands in _yield_result_and_operands(input_file_path)
        if _is_equation_possible(result, operands, ["*", "+"])
    )


@register_solution(2024, 7, 2)
def part_two(input_file_path: str) -> int:
    return sum(
        result
        for result, operands in _yield_result_and_operands(input_file_path)
        if _is_equation_possible(result, operands, ["*", "+", "||"])
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 7)
    part_one(input_file_path)
    part_two(input_file_path)
