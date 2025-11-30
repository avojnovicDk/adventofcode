from collections import defaultdict
from itertools import combinations
from typing import Generator
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _yield_lan_parties(connections: dict[str, set[str]], length: int) -> Generator[set[str], None, None]:
    possible_lan_parties = set(
        frozenset(sorted([k] + list(v)))
        for k, v in connections.items()
        if len(v) + 1 >= length
    )
    is_lan_party = lambda p: all(connections[n].issuperset(p - {n}) for n in p)

    yield from (
        party - set(c)
        for party in possible_lan_parties
        for c in combinations(party, r=len(party) - length)
        if is_lan_party(party - set(c))
    )


def _get_connections(input_file_path: str) -> dict[str, set[str]]:
    connections = defaultdict(set)
    for line in yield_lines(input_file_path):
        x, y = line.strip().split("-")
        connections[x].add(y)
        connections[y].add(x)
    
    return connections


@register_solution(2024, 23, 1)
def part_one(input_file_path: str) -> int:
    connections = _get_connections(input_file_path)

    return len(
        set(
            lan_party
            for lan_party in _yield_lan_parties(connections, 3)
            if any(c[0] == "t" for c in lan_party)
        )
    )


@register_solution(2024, 23, 2)
def part_two(input_file_path: str) -> str:
    connections = _get_connections(input_file_path)

    return (
        ",".join(
            sorted(
                next(
                    lan_party
                    for length in range(len(connections), 0, -1)
                    for lan_party in _yield_lan_parties(connections, length)
                )
            )
        )
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 23)
    part_one(input_file_path)
    part_two(input_file_path)
