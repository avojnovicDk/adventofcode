from collections import namedtuple
from copy import deepcopy
from itertools import combinations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


Operation = namedtuple("Operation", ["o1", "o", "o2", "r"])


@register_solution(2024, 24, 1)
def part_one(input_file_path: str):
    line_yielder = yield_lines(input_file_path)

    wires = dict()
    for wire_value in line_yielder:
        if not wire_value.strip():
            break
        wire, value = wire_value.split(":")
        wires[wire] = int(value.strip())
    
    operations = set()
    for operation in line_yielder:
        o1, o, o2, _, r = operation.split()
        operations.add(Operation(o1, o, o2, r))

    while any(o for o in operations if o.r.startswith("z")):
        o = next(o for o in operations if o.o1 in wires and o.o2 in wires)
        match o.o:
            case "AND":
                wires[o.r] = wires[o.o1] & wires[o.o2]
            case "OR":
                wires[o.r] = wires[o.o1] | wires[o.o2]
            case "XOR":
                wires[o.r] = wires[o.o1] ^ wires[o.o2]
        operations.remove(o)

    return sum(
        pow(2, int(w[1:]))
        for w, v in wires.items()
        if v and w.startswith("z")
    )


def _run_operations(wires, operations):
    while any(o for o in operations if o.r.startswith("z")):
        o = next(o for o in operations if o.o1 in wires and o.o2 in wires)
        match o.o:
            case "AND":
                wires[o.r] = wires[o.o1] & wires[o.o2]
            case "OR":
                wires[o.r] = wires[o.o1] | wires[o.o2]
            case "XOR":
                wires[o.r] = wires[o.o1] ^ wires[o.o2]
        operations.remove(o)

@register_solution(2024, 24, 2)
def part_two(input_file_path: str):
    line_yielder = yield_lines(input_file_path)

    wires = dict()
    for wire_value in line_yielder:
        if not wire_value.strip():
            break
        wire, value = wire_value.split(":")
        wires[wire] = int(value.strip())
    
    kept_wires = deepcopy(wires)

    x = [v for _, v in sorted(((w, v) for w, v in wires.items() if w.startswith("x")), reverse=True)]
    y = [v for _, v in sorted(((w, v) for w, v in wires.items() if w.startswith("y")), reverse=True)]
    z = [a & b for a, b in zip(x, y)]
    print(x)
    print(y)
    print(z)
    
    operations = set()
    for operation in line_yielder:
        o1, o, o2, _, r = operation.split()
        operations.add(Operation(o1, o, o2, r))

    kept_operations = operations.copy()

    _run_operations(wires, operations)

    z_len = len([w for w in wires.keys() if w.startswith("z")])
    if len(z) > z_len:
        z.pop(0)
    if len (z) < z_len:
        z = [0] + z
    # print(x)
    # print(y)
    # print(z)
    # print(wires)
    # z_res = list(
    #     (w for (w, v), v_correct in 
    #     zip(
    #         sorted(
    #             ((w, v) for w, v in wires.items() if w.startswith("z")),
    #             key=lambda a: int(a[0].replace("z", "")),
    #             reverse=True
    #         ),
    #         z
    #     )
    #     if v != v_correct
    # ))
    # print(z_res)
    # z_len = len([w for w in wires.keys() if w.startswith("z")])
    # if len(z) > z_len:
    #     z.pop(0)

    # from pprint import pprint
    # pprint(wires)
    # assert 33==333

    faulty_outputs = [
        wire
        for wire, value in wires.items()
        if wire.startswith("z")
        if z[int(wire.replace("z", ""))] != value
    ]
    i = 0
    while(i <100):
        i += 1
        operands = set()
        for o in kept_operations:
            if o.r in faulty_outputs:
                operands.add(o.o1)
                operands.add(o.o2)
        print(len([o for o in operands if "x" not in o and "y" not in o]))
        if len([o for o in operands if "x" not in o and "y" not in o]) == 16:
            print(sorted(operands))
        faulty_outputs = operands
            
    assert 44==444
        
    
    z_res = list(
        ((w, v, v_correct) for (w, v), v_correct in 
        zip(
            sorted(
                ((w, v) for w, v in wires.items() if w.startswith("z"))
            ),
            reversed(z)
        )
        # if v != v_correct
    ))
    print(z_res)
    print("***")
    possible_swaps = list(combinations(kept_operations, r=2))
    print("***", len(possible_swaps))
    all_swaps = list(combinations(possible_swaps, r=4))
    print("***")
    for i, swaps in enumerate(all_swaps):
        print(f"{i}/{len(all_swaps)}")
        if len(set(s.r for swap in swaps for s in swap)) < 8:
            continue
        wires, operations = deepcopy(kept_wires), kept_operations.copy()
        for swap1, swap2 in swaps:
            o1 = [o for o in operations if o == swap1][0]
            o2 = [o for o in operations if o == swap2][0]
            operations.add(Operation(o1.o1, o1.o, o1.o2, o2.r))
            operations.add(Operation(o2.o1, o2.o, o2.o2, o1.r))
            operations.remove(o1)
            operations.remove(o2)
            
        # has_found = False
        # print([s.r for swap in swaps for s in swap])
        # if [s.r for swap in swaps for s in swap] in (['z00', 'z05', 'z02', 'z01'], ['z05', 'z00', 'z02', 'z01'], ['z01', 'z02', 'z05', 'z00'], ['z02', 'z01', 'z05', 'z00'], ['z05', 'z00', 'z01', 'z02']):
        #     has_found = True
        #     from pprint import pprint
        #     print(swaps)
        #     pprint(wires)
        #     pprint(operations)
        try:
            _run_operations(wires, operations)
        except StopIteration:
            continue
        
        # if has_found:
        #     from pprint import pprint
        #     pprint(wires)
        #     assert 33==3333
        z_res = list(
            (w for (w, v), v_correct in 
            zip(
                sorted(
                    ((w, v) for w, v in wires.items() if w.startswith("z")),
                    key=lambda a: -int(a[0].replace("z", "")),
                ),
                z
            )
            if v != v_correct
        ))
        
        if not z_res:
            # print("FOUND")
            # from pprint import pprint
            # pprint(swaps)
            # print(x)
            # print(y)
            # print(z)
            # print(sorted(
            #         ((w, v) for w, v in wires.items() if w.startswith("z")),
            #         key=lambda a: -int(a[0].replace("z", ""))
            #     ))
            return ",".join(sorted(s.r for swap in swaps for s in swap))
            break

    return sum(
        pow(2, int(w[1:]))
        for w, v in wires.items()
        if v and w.startswith("z")
    )

@register_solution(2024, 24, 2)
def part_two(input_file_path: str):
    line_yielder = yield_lines(input_file_path)

    wires = dict()
    for wire_value in line_yielder:
        if not wire_value.strip():
            break
        wire, value = wire_value.split(":")
        wires[wire] = int(value.strip())
    
    kept_wires = deepcopy(wires)

    x = [v for _, v in sorted(((w, v) for w, v in wires.items() if w.startswith("x")), reverse=True)]
    y = [v for _, v in sorted(((w, v) for w, v in wires.items() if w.startswith("y")), reverse=True)]
    z = []
    res = 0
    for a, b in reversed(list(zip(x, y))):
        s = a + b + res
        match s:
            case 2:
                z.append(0)
                res = 1
            case 3:
                z.append(1)
                res = 1
            case _:
                z.append(s)
                res = 0
    z.append(res)
    z = list(reversed(z))
    print(" " + "".join(map(str, x)))
    print(" " + "".join(map(str, y)))
    print("".join(map(str, z)))

    operations = set()
    for operation in line_yielder:
        o1, o, o2, _, r = operation.split()
        operations.add(Operation(o1, o, o2, r))

    kept_operations = operations.copy()

    _run_operations(wires, operations)

    # z_len = len([w for w in wires.keys() if w.startswith("z")])
    # if len(z) > z_len:
    #     z.pop(0)
    # if len (z) < z_len:
    #     z = [0] + z
    # print(x)
    # print(y)
    # print(z)
    # print(wires)
    # z_res = list(
    #     (w for (w, v), v_correct in 
    #     zip(
    #         sorted(
    #             ((w, v) for w, v in wires.items() if w.startswith("z")),
    #             key=lambda a: int(a[0].replace("z", "")),
    #             reverse=True
    #         ),
    #         z
    #     )
    #     if v != v_correct
    # ))
    # print(z_res)
    # z_len = len([w for w in wires.keys() if w.startswith("z")])
    # if len(z) > z_len:
    #     z.pop(0)

    # from pprint import pprint
    # pprint(wires)
    # assert 33==333

    faulty_outputs = [
        wire
        for wire, value in wires.items()
        if wire.startswith("z")
        if z[int(wire.replace("z", ""))] != value
    ]
    i = 0
    possible_outputs = set(faulty_outputs)
    while(i <100):
        i += 1
        operands = set()
        for o in kept_operations:
            if o.r in faulty_outputs:
                operands.add(o.o1)
                operands.add(o.o2)
        possible_outputs |= operands
        # print(len([o for o in operands if "x" not in o and "y" not in o]))
        # if len([o for o in operands if "x" not in o and "y" not in o]) == 16:
        #     print(sorted(operands))
        faulty_outputs = operands
    
    print(possible_outputs, len(possible_outputs))
        
    
    z_res = list(
        ((w, v, v_correct) for (w, v), v_correct in 
        zip(
            sorted(
                ((w, v) for w, v in wires.items() if w.startswith("z"))
            ),
            reversed(z)
        )
        # if v != v_correct
    ))
    print(z_res)
    print("***", len(possible_outputs))
    
    ops = (o for o in kept_operations if o.r in possible_outputs)
    possible_swaps = list(combinations(ops, r=2))
    print("***", len(possible_swaps))
    all_swaps = list(combinations(possible_swaps, r=4))
    print("***")
    for i, swaps in enumerate(all_swaps):
        print(f"{i}/{len(all_swaps)}")
        if len(set(s.r for swap in swaps for s in swap)) < 8:
            continue
        wires, operations = deepcopy(kept_wires), kept_operations.copy()
        for swap1, swap2 in swaps:
            o1 = [o for o in operations if o == swap1][0]
            o2 = [o for o in operations if o == swap2][0]
            operations.add(Operation(o1.o1, o1.o, o1.o2, o2.r))
            operations.add(Operation(o2.o1, o2.o, o2.o2, o1.r))
            operations.remove(o1)
            operations.remove(o2)
            
        # has_found = False
        # print([s.r for swap in swaps for s in swap])
        # if [s.r for swap in swaps for s in swap] in (['z00', 'z05', 'z02', 'z01'], ['z05', 'z00', 'z02', 'z01'], ['z01', 'z02', 'z05', 'z00'], ['z02', 'z01', 'z05', 'z00'], ['z05', 'z00', 'z01', 'z02']):
        #     has_found = True
        #     from pprint import pprint
        #     print(swaps)
        #     pprint(wires)
        #     pprint(operations)
        try:
            _run_operations(wires, operations)
        except StopIteration:
            continue
        
        # if has_found:
        #     from pprint import pprint
        #     pprint(wires)
        #     assert 33==3333
        z_res = list(
            (w for (w, v), v_correct in 
            zip(
                sorted(
                    ((w, v) for w, v in wires.items() if w.startswith("z")),
                    key=lambda a: -int(a[0].replace("z", "")),
                ),
                z
            )
            if v != v_correct
        ))
        
        if not z_res:
            # print("FOUND")
            # from pprint import pprint
            # pprint(swaps)
            # print(x)
            # print(y)
            # print(z)
            # print(sorted(
            #         ((w, v) for w, v in wires.items() if w.startswith("z")),
            #         key=lambda a: -int(a[0].replace("z", ""))
            #     ))
            return ",".join(sorted(s.r for swap in swaps for s in swap))
            break

    return sum(
        pow(2, int(w[1:]))
        for w, v in wires.items()
        if v and w.startswith("z")
    )


@register_solution(2024, 24, 2)
def part_two(input_file_path: str):
    line_yielder = yield_lines(input_file_path)

    wires = dict()
    for wire_value in line_yielder:
        if not wire_value.strip():
            break
        wire, value = wire_value.split(":")
        wires[wire] = int(value.strip())

    operations = set()
    for operation in line_yielder:
        o1, o, o2, _, r = operation.split()
        if o1.startswith("y") and o2.startswith("x"):
            o1, o2 = o2, o1
        operations.add(Operation(o1, o, o2, r))



    dnt,gdf,gwc,jst,mcm,z05,z15,z30
    o1 = [o for o in operations if o.r == "jst"][0]
    o2 = [o for o in operations if o.r == "z05"][0]
    operations.add(Operation(o1.o1, o1.o, o1.o2, o2.r))
    operations.add(Operation(o2.o1, o2.o, o2.o2, o1.r))
    operations.remove(o1)
    operations.remove(o2)
    

    o1 = [o for o in operations if o.r == "mcm"][0]
    o2 = [o for o in operations if o.r == "gdf"][0]
    operations.add(Operation(o1.o1, o1.o, o1.o2, o2.r))
    operations.add(Operation(o2.o1, o2.o, o2.o2, o1.r))
    operations.remove(o1)
    operations.remove(o2)

    o1 = [o for o in operations if o.r == "dnt"][0]
    o2 = [o for o in operations if o.r == "z15"][0]
    operations.add(Operation(o1.o1, o1.o, o1.o2, o2.r))
    operations.add(Operation(o2.o1, o2.o, o2.o2, o1.r))
    operations.remove(o1)
    operations.remove(o2)

    o1 = [o for o in operations if o.r == "gwc"][0]
    o2 = [o for o in operations if o.r == "z30"][0]
    operations.add(Operation(o1.o1, o1.o, o1.o2, o2.r))
    operations.add(Operation(o2.o1, o2.o, o2.o2, o1.r))
    operations.remove(o1)
    operations.remove(o2)

    x = [v for _, v in sorted(((w, v) for w, v in wires.items() if w.startswith("x")), reverse=True)]
    y = [v for _, v in sorted(((w, v) for w, v in wires.items() if w.startswith("y")), reverse=True)]
    print("".join(map(str, x)))
    print("".join(map(str, y)))


    from pprint import pprint

    x_and_y = sorted(
        (
            o
            for o in operations
            if ("x" in o.o1 or "y" in o.o1) and ("x" in o.o2 or "y" in o.o2)
        ),
        key=lambda x: (x.o, x.o1, x.o2)
    )
    for_sum_out = sorted((o2 for o1 in x_and_y if o1.o == "XOR" for o2 in operations if o1.r in (o2.o1, o2.o2) and o2.o == "XOR"), key=lambda x: x.r)
    # pprint(x_and_y)
    # pprint(for_sum_out)
    # print([o for o in operations if o.r=="z00"])
    # print([o for o in operations if o.r=="z30"])
    # print([o2 for o1 in operations if o1.r=="z30" for o2 in operations if o2.r in (o1.o1, o1.o2)])
    # # print([o for o in operations if o.o1.startswith("x30")])
    # # print([o for o in operations if o.o2.startswith("fhg")])
    # print([o for o in operations if o.r.startswith("gwc")])
    # print([o for o in operations if o.r.startswith("dnt")])
    # print([o for o in operations if o.r.startswith("ckf")])
    _run_operations(wires, operations)
    from pprint import pprint
    # pprint(wires)
    print("01010110101100111110110010110001100011011100110")
    z = [v for _, v in sorted(((w, v) for w, v in wires.items() if w.startswith("z")), reverse=True)]
    print("0" + "".join(map(str, z)))



if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 24)
    part_one(input_file_path)
    part_two(input_file_path)
