from functools import reduce
from typing import Callable, Optional

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


class SafetyChecker:
    is_increasing: Optional[bool] = None
    index: int = 0

    def __call__(self, prev_el: int, el: int):
        if prev_el == el:
            raise Exception()

        if self.is_increasing is None:
            self.is_increasing = el > prev_el
        elif self.is_increasing and el < prev_el:
            raise Exception()
        elif not self.is_increasing and el > prev_el:
            raise Exception()
        
        if abs(el - prev_el) > 3:
            raise Exception()
        
        self.index += 1

        return el
    

def _check_line_safety(line: list[int], unsafe_handler: Callable):
    check = SafetyChecker()
    try:
        reduce(check, line)
    except Exception:
        return unsafe_handler(check, line)
    else:
        return True


def _count_safe_lines(input_file_path: str, unsafe_handler: Callable):
    return sum(
        1
        for line in yield_lines(input_file_path)
        if _check_line_safety(list(map(int, line.split())), unsafe_handler)
    )


@register_solution(2024, 2, 1)
def part_one(input_file_path: str):
    return _count_safe_lines(input_file_path, lambda a, b: False)


@register_solution(2024, 2, 2)
def part_two(input_file_path: str):
    def _remove_one_and_retry(check: SafetyChecker, line: list[int]):
        for i in (check.index - 1, check.index, check.index + 1):
            curr_line = list(line)
            curr_line.pop(i)
            try:
                reduce(SafetyChecker(), curr_line)
            except Exception:
                pass
            else:
                return True
        return False
    
    return _count_safe_lines(input_file_path, _remove_one_and_retry)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 2)
    part_one(input_file_path)
    part_two(input_file_path)
