from collections import defaultdict

from adventofcode.registry.decorators import register_solution
from adventofcode.util.helpers import solution_profiler
from adventofcode.util.input_helpers import yield_lines


class PageOrderer:
    def __init__(self, rules_yielder):
        self.pages_after = defaultdict(set)
        line = next(rules_yielder).strip()
        while(line):
            p1, p2 = line.split("|")
            self.pages_after[p1].add(p2)
            line = next(rules_yielder).strip()

    def _detect_forbidden_index(self, pages):
        visited_pages = set()
        for i, p in enumerate(pages):
            if self.pages_after[p] & visited_pages:
                return i
            visited_pages.add(p)

    def is_valid(self, pages):
        return not self._detect_forbidden_index(pages)
    
    def correct(self, pages):
        i = self._detect_forbidden_index(pages)
        while i:
            j = pages.index(next(iter(set(pages[:i]) & self.pages_after[pages[i]])))
            pages[i], pages[j] = pages[j], pages[i]
            i = self._detect_forbidden_index(pages)
        return pages


def _sum_middle_page_numbers(input_file_path: str, are_updates_valid: bool) -> int:
    line_yielder = yield_lines(input_file_path)
    page_orderer = PageOrderer(line_yielder)

    updates = (update.strip().split(",") for update in line_yielder)
    updates = filter(lambda u: page_orderer.is_valid(u) is are_updates_valid, updates)
    if not are_updates_valid:
        updates = map(page_orderer.correct, updates)

    return sum(int(u[len(u)//2]) for u in updates)


@register_solution(2024, 5, 1)
def part_one(input_file_path: str):
    return _sum_middle_page_numbers(input_file_path, True)


@register_solution(2024, 5, 2)
def part_two(input_file_path: str):
    return _sum_middle_page_numbers(input_file_path, False)
