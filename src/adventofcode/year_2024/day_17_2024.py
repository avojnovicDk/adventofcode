from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _part_one(registry: dict[str, int], program: str):
    instuctions = program.split(",")
    output = list()
    pointer = 0
    while pointer < len(instuctions):
        opcode, literal = int(instuctions[pointer]), int(instuctions[pointer + 1])
        combo = literal
        pointer += 2
        match literal:
            case 4:
                combo = registry["A"]
            case 5:
                combo = registry["B"]
            case 6:
                combo = registry["C"]
        match opcode:
            case 0:
                registry["A"] = registry["A"] // pow(2, combo)
            case 1:
                registry["B"] ^= literal
            case 2:
                registry["B"] = combo % 8
            case 3:
                if registry["A"]:
                    pointer = literal
            case 4:
                registry["B"] ^= registry["C"]
            case 5:
                output.append(combo % 8)
            case 6:
                registry["B"] = registry["A"] // pow(2, combo)
            case 7:
                registry["C"] = registry["A"] // pow(2, combo)
    return ",".join(str(o) for o in output)


@register_solution(2024, 17, 1)
def part_one(input_file_path: str):
    registry = dict()
    line_yielder = yield_lines(input_file_path)
    line = next(line_yielder).strip()
    while line:
        r, v = line.replace("Register ", "").split(":")
        registry[r.strip()] = int(v.strip())
        line = next(line_yielder).strip()
    program = next(line_yielder).strip()
    program = program.replace("Program: ", "")
    return _part_one(registry, program)


@register_solution(2024, 17, 2)
def part_two(input_file_path: str):
    registry = dict()
    line_yielder = yield_lines(input_file_path)
    line = next(line_yielder).strip()
    while line:
        r, v = line.replace("Register ", "").split(":")
        registry[r.strip()] = int(v.strip())
        line = next(line_yielder).strip()
    program = next(line_yielder).strip()
    program = program.replace("Program: ", "")
    for a in range (0, 1000000):
        registry["A"] = a
        if _part_one(registry, program) == program:
            return a


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 17)
    part_one(input_file_path)
    part_two(input_file_path)
