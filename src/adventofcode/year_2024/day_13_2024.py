from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _calc_price(input_file_path: str, extra_prize: int = 0) -> int:
    price = 0

    line_yielder = None
    while line_yielder is None or next(line_yielder, None):
        if line_yielder is None:
            line_yielder = yield_lines(input_file_path)

        a_x, a_y = map(int, next(line_yielder).replace("Button A: X+", "").replace(" Y+", "").split(","))
        b_x, b_y = map(int, next(line_yielder).replace("Button B: X+", "").replace(" Y+", "").split(","))
        p_x, p_y = map(int, next(line_yielder).replace("Prize: X=", "").replace(" Y=", "").split(","))
        p_x, p_y = p_x + extra_prize, p_y + extra_prize
        
        y = (p_y * a_x - p_x * a_y) / (b_y * a_x - a_y * b_x)
        if y == int(y):
            x = (p_x - b_x * y) / a_x
            if x == int(x):
                price += int(3 * x + y)

    return price


@register_solution(2024, 13, 1)
def part_one(input_file_path: str) -> int:
    return _calc_price(input_file_path)


@register_solution(2024, 13, 2)
def part_two(input_file_path: str) -> int:
    return _calc_price(input_file_path, 10000000000000)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 13)
    part_one(input_file_path)
    part_two(input_file_path)
