from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _is_design_possible(design: str, towels: list[str]):
    for towel in towels:
        if not design.startswith(towel):
            continue
        if not design.replace(towel, ""):
            return True
        if _is_design_possible(design.replace(towel, "", 1), towels):
            return True
    return False

def _get_possible_designs(design: str, towels: list[str]):
    print("&&&")
    return 3
    possible_towels = [t for t in towels if t in design]
    towels_design_starts_with = [t for t in possible_towels if design.startswith(t)]
    # if not towels_design_starts_with:
    #     return 0
    sum_all = 0
    for towel in towels_design_starts_with:
        print(design, towel)
        if design.replace(towel, ""):
            sum_all += 1
        else:
            sum_all += _yield_possible_designs(design.replace(towel, "", 1), possible_towels)
    return sum_all
    return list(
        (1 if not design.replace(towel, "") else _yield_possible_designs(design.replace(towel, "", 1), possible_towels))
        for towel in towels_design_starts_with
    )
    for towel in possible_towels:
        if not design.startswith(towel):
            continue
        if not design.replace(towel, ""):
            yield 1
        yield from _yield_possible_designs(design.replace(towel, "", 1), towels)


@register_solution(2024, 19, 1)
def part_one(input_file_path: str):
    line_yielder = yield_lines(input_file_path)

    possible_towels = next(line_yielder).strip().split(", ")
    next(line_yielder)
    return sum(1 if _is_design_possible(design.strip(), possible_towels) else 0 for design in line_yielder)
        

@register_solution(2024, 19, 2)
def part_two(input_file_path: str):
    line_yielder = yield_lines(input_file_path)

    possible_towels = next(line_yielder).strip().split(", ")
    next(line_yielder)
    for design in line_yielder:
        print(design.strip())
        a = _get_possible_designs(design.strip(), possible_towels)
        print(a)
    # return sum(_yield_possible_designs(design.strip(), possible_towels) for design in line_yielder)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 19)
    part_one(input_file_path)
    part_two(input_file_path)
