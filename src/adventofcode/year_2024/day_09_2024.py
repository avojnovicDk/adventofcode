from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, read_file


def _take_next_right(input, r_id, r_len):
    r_len = input.pop()
    input.pop()
    return r_id - 1, r_len


def _yield_moved(input, l_len, r_len, right):
    while l_len:
        if r_len == 0:
            right, r_len = _take_next_right(input, right, r_len)
        
        if r_len < l_len:
            yield (r_len, right)
            l_len -= r_len
            right, r_len = _take_next_right(input, right, r_len)

        if r_len >= l_len:
            yield (l_len, right)
            r_len -= l_len
            l_len = 0

    return r_len, right


def _yield_defragmented_by_one(input, r_id):
    l_id = -1
    r_id += 1
    r_len = 0

    while input:
        l_id += 1
        yield (input.pop(0), l_id)

        if input:
            yielder = _yield_moved(input, input.pop(0), r_len, r_id)
            r_len, r_id = yield from yielder

    if r_len:
        yield (r_len, r_id)


@register_solution(2024, 9, 1)
def part_one(input_file_path: str):
    input = [int(el) for el in read_file(input_file_path)]

    checksum, position = 0, 0
    for length, id in _yield_defragmented_by_one(input, len(input) // 2):
        checksum += sum(range(position, position + length)) * id
        position += length
    
    return checksum


def _defragment_by_block(input):
    for r_len, r_id in filter(lambda x: x[1] is not None, input[::-1]):
        i = input.index((r_len, r_id))
        try:
            j, l_len = next(
                (j, l_len) 
                for j, (l_len, l_id) in enumerate(input[:i]) 
                if l_id is None and l_len >= r_len
            )
        except StopIteration:
            continue
        input[i] = (r_len, None)
        input[j] = (r_len, r_id)
        if l_len > r_len:
            input.insert(j + 1, (l_len - r_len, None))


@register_solution(2024, 9, 2)
def part_two(input_file_path: str):
    input = [
        (int(el), i // 2 if i % 2 == 0 else None)
        for i, el in enumerate(read_file(input_file_path))   
    ]
    _defragment_by_block(input)
    checksum, position = 0, 0
    for length, id in input:
        if id is not None:
            checksum += sum(range(position, position + length)) * id
        position += length
    
    return checksum


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 9)
    part_one(input_file_path)
    part_two(input_file_path)
