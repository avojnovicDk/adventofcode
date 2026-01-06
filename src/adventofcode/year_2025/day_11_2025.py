from collections import defaultdict

from adventofcode.registry.decorators import register_solution
from adventofcode.util.helpers import memoize
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def find_out(pos, graph):
    return pos == "out" or sum(find_out(c, graph) for c in graph[pos])


class PathCounter:
    def __init__(self, graph):
        self.graph = graph

    @memoize
    def __call__(self, pos, dest):
        return pos == dest or sum(self(c, dest) for c in self.graph[pos])


def _get_graph(file_path):
    graph = defaultdict(set)
    for line in yield_lines(file_path):
        source, dests = line.strip().split(':')
        graph[source] = set(dests.strip().split(' '))
    return graph


@register_solution(2025, 11, 1)
def part_one(input_file_path: str):
    return find_out("you", _get_graph(input_file_path))
    

@register_solution(2025, 11, 2)
def part_two(input_file_path: str):
    path_counter = PathCounter(_get_graph(input_file_path))
    
    return (
        path_counter("svr", "fft")
        * path_counter("fft", "dac")
        * path_counter("dac", "out")
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 11)
    part_one(input_file_path)
    part_two(input_file_path)
