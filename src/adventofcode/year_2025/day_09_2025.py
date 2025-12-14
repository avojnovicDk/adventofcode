from collections import defaultdict, namedtuple
from itertools import combinations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


Point = namedtuple("Point", "row col")


@register_solution(2025, 9, 1)
def part_one(input_file_path: str):
    rectangles = {tuple(map(int, r.split(','))) for r in yield_lines(input_file_path)}
    return max((abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1) for a, b in combinations(rectangles, 2))


def part_ddtwo(input_file_path: str):
    rectangles = [tuple(map(int, r.split(','))) for r in yield_lines(input_file_path)]
    allowed = set()
    for a, b in zip(rectangles, rectangles[1:] + [rectangles[-1]]):
        if a[0] == b[0]:
            allowed |= set(a[0] + x * 1j for x in range(min(a[1], b[1]), max(a[1], b[1]) + 1))
        else:
            allowed |= set(x + a[1] * 1j for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1))

    dim_x = max(i[0] for i in rectangles)
    dim_y = max(i[1] for i in rectangles)

    for x in range(dim_x):
        is_in = False
        for y in range(dim_y):
            p = x + y * 1j
            # if (x == 9):
            #     print(p, is_in, p in allowed)
            if not is_in and p in allowed:
                is_in = True
            elif is_in and p in allowed:
                is_in = False
            elif is_in and p not in allowed:
                allowed.add(p)

    for a in sorted(list(allowed), key= lambda x: (x.real, x.imag)):
        print(a)


    max_area = 0
    for a, b in combinations(rectangles, 2):
        if a[0] != b[0] and a[1] != b[1]:
            other_corners = {b[0] + a[1] * 1j, a[0] + b[1] * 1j}
        else:
            other_corners = set()
        if a == (9, 5) and b == (2, 3):
            print(a, b, other_corners, allowed.issuperset(other_corners))
        if allowed.issuperset(other_corners):
            area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            if area > max_area:
                max_area = area
    
    return max_area


def _check_in_frame(point, frame):
    if point in frame:
        return True
    
    x, y = point
    ys = sorted(p[1] for p in frame if p[0] == x and p[1] <= y)
    if point == (7, 7):
        print([p for p in frame if p[0] == x])
        print(ys)

    try:
        first = ys.pop(0)
    except IndexError:
        return False
    
    if point == (7, 7):
        print(first)

    is_in = True
    curr = first
    while ys:
        try:
            while (next := ys.pop(0)) == curr + 1:
                curr = next
        except IndexError:
            pass
        
        if curr < y < next:
            return is_in
        curr = next
        is_in = not is_in
        if point == (7, 7):
            print(is_in, ys)
    
    return is_in


def part_sstwo(input_file_path: str):
    rectangles = [tuple(map(int, r.split(','))) for r in yield_lines(input_file_path)]
    frame = set()
    for a, b in zip(rectangles, rectangles[1:] + [rectangles[0]]):
        if a[0] == b[0]:
            frame |= set((a[0], x) for x in range(min(a[1], b[1]), max(a[1], b[1]) + 1))
        else:
            frame |= set((x, a[1]) for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1))


    print(a, b)
    print("***  ")

    max_area = 0
    for a, b in combinations(rectangles, 2):
        # if b == (2, 5) and a == (11, 1):
        #     print(")))))", _check_in_frame((b[0], a[1]), frame), _check_in_frame((a[0], b[1]), frame))
        if _check_in_frame((b[0], a[1]), frame) and _check_in_frame((a[0], b[1]), frame):
            area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            if area == 35:
                print(a, b, _check_in_frame((7, 7), frame))
            if area > max_area:
                max_area = area

    return max_area


def _get_allowed(allowed):
    is_in = False
    result = []
    for nxt in sorted(allowed):
        if nxt[0] == nxt[1]:
            if not is_in:
                is_in = True
                curr = nxt
            elif nxt[0] == curr[1]:
                continue
            else:
                is_in = False
                result.append((curr[0], nxt[1]))
        else:
            if not is_in:
                is_in = True
                curr = nxt
            else:
                is_in = False
                result.append((curr[0], nxt[1]))
    if is_in:
        result.append(curr)
    return result


def _check_is_inside(point, allowed_per_row):
    row = list(allowed_per_row[point[1]])
    counter = 0
    while row:
        nxt = row.pop()
        if nxt[1] < point[0]:
            continue
        if nxt[0] <= point[0] <= nxt[1]:
            return True
        if nxt[0] == nxt[1]:
            counter += 1
    if point == (15109, 85878)  or point == (83065, 15883):
        print(allowed_per_row[point[1]], point, counter, counter % 2 != 0)
    return counter % 2 != 0
    



# @register_solution(2025, 9, 2)
def psart_two(input_file_path: str):
    rectangles = [tuple(map(int, r.split(','))) for r in yield_lines(input_file_path)]
    allowed_per_row = defaultdict(set)
    for a, b in zip(rectangles, rectangles[1:] + [rectangles[0]]):
        if a[1] == b[1]:
            allowed_per_row[a[1]].add((min(a[0], b[0]), max(a[0], b[0])))
        else:
            for row in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                allowed_per_row[row].add((a[0], a[0]))
    
    # allowed_per_row = {row: _get_allowed(allowed) for row, allowed in allowed_per_row.items()}

    # from pprint import pprint
    # pprint(allowed_per_row)

    max_area = 0
    for a, b in combinations(rectangles, 2):
        # if b == (2, 5) and a == (11, 1):
        #     print(")))))", _check_in_frame((b[0], a[1]), frame), _check_in_frame((a[0], b[1]), frame))
        if _check_is_inside((a[0], b[1]), allowed_per_row) and _check_is_inside((b[0], a[1]), allowed_per_row):
            area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            if area > max_area:
                max_area = area
                if area == 4756718172:
                    print(a, b)
                # if area == 4599890450:

    return max_area


def _get_count_for_line(line, row, allowed_per_row):
    return len(set(line) - allowed_per_row[row + 1])


def _check_is_inside(point, allowed_per_row):
    check_points = [(83664, 84156), (15810, 16367)]
    x, row = point
    allowed = sorted(allowed_per_row[row], key=lambda p: p[0] if isinstance(p, tuple) else p)
    # if point in check_points:
    #     print(point, allowed)
    while allowed:
        nxt = allowed.pop(0)
        if (nxt[1] if isinstance(nxt, tuple) else nxt) >= x:
            break

    if (nxt[1] if isinstance(nxt, tuple) else nxt) < x:
        return False
    
    # if point in check_points:
    #     print(point, nxt, allowed)

    if isinstance(nxt, tuple):
        if nxt[0] <= x <= nxt[1]:
            return True
    else:
        if nxt == x:
            return True
    
    # for a in allowed:
    #     if point in check_points and isinstance(a, tuple):
    #         l, r = a
    #         print({l, r} - allowed_per_row[row + 1])
            # print(l, r, allowed_per_row[row + 1])
            # print(l, r, allowed_per_row[row - 1])

    # if point == (2, 1) or point == (11, 5):
    #     print(point, (len([a for a in allowed if not isinstance(a, tuple)]) + (0 if isinstance(nxt, tuple) else 0)), allowed)
    allowed.append(nxt)
    counter = 0
    for a in allowed:
        if isinstance(a, tuple):
            # if point in check_points:
            #     print(point, a, allowed_per_row[row-1])
            #     print(point, a, allowed_per_row[row+1])
            counter += len(set(a) - allowed_per_row[row + 1])
        else:
            counter += 1
    if point in check_points:
        print(allowed, counter)
    return counter % 2 == 1


def part_twdddo(input_file_path: str):
    rectangles = [tuple(map(int, r.split(','))) for r in yield_lines(input_file_path)]
    allowed_per_row = defaultdict(set)
    # max_col = max(c[0] for c in rectangles) + 1
    # print(max_col)
    for a, b in zip(rectangles, rectangles[1:] + [rectangles[0]]):
        if a[0] == b[0]:
            for row in range(min(a[1], b[1]) + 1, max(a[1], b[1])):
                allowed_per_row[row].add(a[0])
        else:
            allowed_per_row[a[1]].add((min(a[0], b[0]), max(a[0], b[0])))

    # for row, allowed in allowed_per_row.items():
    #     row = ['.'] * max_col
    #     for a in allowed:
    #         if isinstance(a, tuple):
    #             row[a[0]] = "X"
    #             row[a[1]] = "X"
    #             for x in range(a[0] + 1, a[1]):
    #                 row[x] = "#"
    #         else:
    #             row[a] = "#"
    #     print("".join(row))

    # from pprint import pprint
    # pprint(allowed_per_row)
    # assert 11==1111
        # if a[1] == b[1]:
        #     allowed_per_row[a[1]].add((min(a[0], b[0]), max(a[0], b[0])))
        # else:
        #     for row in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
        #         allowed_per_row[row].add((a[0], a[0]))
    
    # allowed_per_row = {row: _get_allowed(allowed) for row, allowed in allowed_per_row.items()}

    # from pprint import pprint
    # pprint(allowed_per_row)

    max_area = 0
    for a, b in combinations(rectangles, 2):
        # if b == (2, 5) and a == (11, 1):
        #     print(")))))", _check_in_frame((b[0], a[1]), frame), _check_in_frame((a[0], b[1]), frame))
        


        if _check_is_inside((a[0], b[1]), allowed_per_row) and _check_is_inside((b[0], a[1]), allowed_per_row):
            area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            if area > max_area:
                max_area = area
                if area == 4599890450:
                    print(a, b)
                #     print(a, b)
                # if area == 4599890450:

    return max_area




def part_tswo(input_file_path: str):
    corners = [tuple(map(int, r.split(','))) for r in yield_lines(input_file_path)]
    valid_points = set()
    max_row, max_col = max(r[1] for r in corners), max(r[0] for r in corners)

    for a, b in zip(corners, corners[1:] + [corners[0]]):
        if a[0] == b[0]:
            for row in range(min(a[1], b[1]) + 1, max(a[1], b[1])):
                valid_points.add((a[0], row))
        else:
            valid_points.add(((min(a[0], b[0]), max(a[0], b[0])), a[1]))
    
    print((max_col, max_row) in corners)


    final_points = set()
    for row in range(max_row + 1):
        print(row, max_row)
        print([p[0] for p in valid_points if p[1] == row])
        # row_points = sorted([p[0] for p in valid_points if p[1] == row], key=lambda: x = x[0] if isinstance(x, tuple) else x)
        print(row_points, "***")
        while row_points:
            first = row_points.pop(0)
            try:
                second = row_points.pop(0)
            except IndexError:
                second = None
            if isinstance(first, tuple):
                final_points |= set((p, row) for p in range (first[0], first[1] + 1))
            else:
                final_points.add((first, row))
            end_first = first[1] + 1 if isinstance(first, tuple) else first
            
            if second:
                if isinstance(second, tuple):
                    final_points |= set((p, row) for p in range (second[0], second[1] + 1))
                else:
                    final_points.add((second, row))
                start_second = second[0] if isinstance(second, tuple) else second
                final_points |= set((i, row) for i in range (end_first + 1, start_second))
    

    for p in sorted(final_points):
        print(p)
        



    print(sorted((j, i) for (i, j) in valid_points))
    assert 33==33333



def _get_starting_point(corners):
    first_row = min(r.row for r in corners)
    first_corner = Point(first_row, min(c.col for c in corners if c.row == first_row))
    assert first_corner in corners
    return Point(first_corner.row + 1, first_corner.col + 1)


def _expand_allowed(pos, allowed):
    to_expand = [pos]
    while to_expand:
        pos = to_expand.pop(0)
        for dir in [Point(0, 1), Point(1, 0), Point(-1, 0), Point(0, -1)]:
            new_pos = Point(pos.row + dir.row, pos.col + dir.col)
            if new_pos not in allowed:
                allowed.add(new_pos)
                to_expand.append(new_pos)



# @register_solution(2025, 9, 2)
def part_twdo(input_file_path: str):
    corners = [Point(int(r.split(',')[1]),int(r.split(',')[0])) for r in yield_lines(input_file_path)]
    borders = set()
    for a, b in zip(corners, corners[1:] + [corners[0]]):
        if a.col == b.col:
            for row in range(min(a.row, b.row), max(a.row, b.row) + 1):
                borders.add(Point(row, a.col))
        else:
            for col in range(min(a.col, b.col), max(a.col, b.col) + 1):
                borders.add(Point(a.row, col))

    starting_point = _get_starting_point(corners)
    
    allowed = {starting_point} | borders
    _expand_allowed(starting_point, allowed)

    # allowed = [(y, x) for (x, y) in allowed]
    # for x in sorted(allowed):
    #     print(x)
    # starting_point = (max_col, max_row)

    # print((max_col, max_row) in corners)

    assert 33==33333




def _check_is_inside(point, allowed_per_row):
    check_points = [(83664, 84156), (15810, 16367)]
    x, row = point
    allowed = sorted(allowed_per_row[row], key=lambda p: p[0] if isinstance(p, tuple) else p)
    # if point in check_points:
    #     print(point, allowed)
    while allowed:
        nxt = allowed.pop(0)
        if (nxt[1] if isinstance(nxt, tuple) else nxt) >= x:
            break

    if (nxt[1] if isinstance(nxt, tuple) else nxt) < x:
        return False
    
    # if point in check_points:
    #     print(point, nxt, allowed)

    if isinstance(nxt, tuple):
        if nxt[0] <= x <= nxt[1]:
            return True
    else:
        if nxt == x:
            return True
    
    # for a in allowed:
    #     if point in check_points and isinstance(a, tuple):
    #         l, r = a
    #         print({l, r} - allowed_per_row[row + 1])
            # print(l, r, allowed_per_row[row + 1])
            # print(l, r, allowed_per_row[row - 1])

    # if point == (2, 1) or point == (11, 5):
    #     print(point, (len([a for a in allowed if not isinstance(a, tuple)]) + (0 if isinstance(nxt, tuple) else 0)), allowed)
    allowed.append(nxt)
    counter = 0
    for a in allowed:
        if isinstance(a, tuple):
            # if point in check_points:
            #     print(point, a, allowed_per_row[row-1])
            #     print(point, a, allowed_per_row[row+1])
            counter += len(set(a) - allowed_per_row[row + 1])
        else:
            counter += 1
    if point in check_points:
        print(allowed, counter)
    return counter % 2 == 1




import tkinter as tk

def draw_lines_tk(vectors, filename='lines.ps',
                  width=800, height=600, margin=20, line_color='black', line_width=2):
    """
    Draw line segments with tkinter Canvas and save to a PostScript file.

    vectors: list of (x1, y1, x2, y2) in your data coordinates
    """
    root = tk.Tk()
    root.title("Line Drawer")
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack()

    # Compute bounds
    xs = [x for (x1, y1, x2, y2) in vectors for x in (x1, x2)]
    ys = [y for (x1, y1, x2, y2) in vectors for y in (y1, y2)]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    span_x = max(max_x - min_x, 1e-9)
    span_y = max(max_y - min_y, 1e-9)

    draw_w = width - 2 * margin
    draw_h = height - 2 * margin
    scale = min(draw_w / span_x, draw_h / span_y)

    def to_canvas(x, y):
        # Map data coords to Canvas pixels; invert Y to keep math-style up
        cx = margin + (x - min_x) * scale
        cy = margin + (max_y - y) * scale
        return cx, cy

    # Draw lines
    for (x1, y1, x2, y2) in vectors:
        cx1, cy1 = to_canvas(x1, y1)
        cx2, cy2 = to_canvas(x2, y2)
        canvas.create_line(cx1, cy1, cx2, cy2, fill=line_color, width=line_width)

    # Save to PostScript
    canvas.postscript(file=filename, colormode='color')
    print(f"Saved PostScript to: {filename}")

    # Close the window (optional)
    root.destroy()



from PIL import Image, ImageDraw

def draw_lines_to_png(segments, filename="lines.png", size=(800, 600), bg="white", rectangle=None):
    """
    segments: list of (x1, y1, x2, y2) in pixel coordinates (top-left origin).
    """
    img = Image.new("RGBA", size, bg)
    draw = ImageDraw.Draw(img)

    for (x1, y1, x2, y2) in segments:
        draw.line((x1, y1, x2, y2), fill="green", width=3)
        draw.circle((x1, y1), radius=3, fill="red")
        draw.circle((x2, y2), radius=3, fill="red")
        if rectangle:
            a, b = rectangle
            c, d = (a[0], b[1]), (b[0], a[1])
            draw.line((a[0], a[1], b), fill="black", width=3)
            draw.line((x1, y1, x2, y2), fill="green", width=3)
            draw.line((x1, y1, x2, y2), fill="green", width=3)
            draw.line((x1, y1, x2, y2), fill="green", width=3)


    img.save(filename)
    return filename

def _check_sides(a, b, row_sides, col_sides):
    # print(a, b, row_sides, col_sides)
    horizontals = (min(a[0], b[0]) + 1, max(a[0], b[0]))
    verticals = (min(a[1], b[1]) + 1, max(a[1], b[1]))

    # print(horizontals)
    for col in range(*horizontals):
        for side in sorted(col_sides[col]):
            if side[0] < a[1] < side[1]:
                return False
            if side[0] < b[1] < side[1]:
                return False
            # print(horizontals, col, side)
    # print(verticals)
    for row in range(*verticals):
        for side in sorted(row_sides[row]):
            if side[0] < a[0] < side[1]:
                return False
            if side[0] < b[0] < side[1]:
                return False
            # print(verticals, row, side)

    # for side in sorted(col_sides[a[1]]):
    #     if side[0] < horizontals[0] < side[1]:
    #         return False
    #     if side[0] >= horizontals[0]:
    #         break
    # for side in sorted(col_sides[b[1]]):
    #     if side[0] < horizontals[0] < side[1]:
    #         return False
    #     if side[0] >= horizontals[0]:
    #         break
    # for side in sorted(row_sides[a[0]]):
    #     if side[0] < verticals[0] < side[1]:
    #         return False
    #     if side[0] >= verticals[0]:
    #         break
    # for side in sorted(row_sides[b[0]]):
    #     if side[0] < verticals[0] < side[1]:
    #         return False
    #     if side[0] >= verticals[0]:
    #         break
    # print(horizontals, a[1], row_sides[a[1]])
    # print(horizontals, b[1], row_sides[b[1]])
    # print(verticals, a[0], col_sides[a[0]])
    # print(verticals, b[0], col_sides[b[0]])

    
    # assert 33==3333
    return True


@register_solution(2025, 9, 2)
def part_two(input_file_path: str):
    rectangles = [tuple(map(int, r.split(','))) for r in yield_lines(input_file_path)]
    allowed_per_row = defaultdict(set)
    max_row = max(c[1] for c in rectangles) + 1
    max_col = max(c[0] for c in rectangles) + 1
    row_sides, col_sides = defaultdict(set), defaultdict(set)
    for a, b in zip(rectangles, rectangles[1:] + [rectangles[0]]):
        if a[0] == b[0]:
            for row in range(min(a[1], b[1]) + 1, max(a[1], b[1])):
                allowed_per_row[row].add(a[0])
            col_sides[a[0]].add((min(a[1], b[1]), max(a[1], b[1])))
        else:
            allowed_per_row[a[1]].add((min(a[0], b[0]), max(a[0], b[0])))
            row_sides[a[1]].add((min(a[0], b[0]), max(a[0], b[0])))

    # for row, allowed in allowed_per_row.items():
    #     row = ['.'] * max_col
    #     for a in allowed:
    #         if isinstance(a, tuple):
    #             row[a[0]] = "X"
    #             row[a[1]] = "X"
    #             for x in range(a[0] + 1, a[1]):
    #                 row[x] = "#"
    #         else:
    #             row[a] = "#"
    #     print("".join(row))

    # from pprint import pprint
    # pprint(allowed_per_row)
    # assert 11==1111
        # if a[1] == b[1]:
        #     allowed_per_row[a[1]].add((min(a[0], b[0]), max(a[0], b[0])))
        # else:
        #     for row in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
        #         allowed_per_row[row].add((a[0], a[0]))
    
    # allowed_per_row = {row: _get_allowed(allowed) for row, allowed in allowed_per_row.items()}

    # from pprint import pprint
    # pprint(allowed_per_row)

    # Example



    max_area = 0
    max_a, max_b = None, None
    for a, b in combinations(rectangles, 2):
        if a[0] == b[0] or a[1] == b[1]:
            continue
        # if b == (2, 5) and a == (11, 1):
        #     print(")))))", _check_in_frame((b[0], a[1]), frame), _check_in_frame((a[0], b[1]), frame))
        


        if _check_is_inside((a[0], b[1]), allowed_per_row) and _check_is_inside((b[0], a[1]), allowed_per_row):
            if _check_sides(a, b, row_sides, col_sides):
                area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
                if area > max_area:
                    max_area = area
                    max_a, max_b = a, b
                    # if area == 4599890450:
                    #     print(a, b)
                    #     print(a, b)
                    # if area == 4599890450:

    segments = []
    for a, b in zip(rectangles, rectangles[1:] + [rectangles[0]]):
        segments.append((a[0] // 100, a[1] // 100, b[0] // 100, b[1] // 100))
    
    out = draw_lines_to_png(segments, "lines.png", size=(1000, 1000), rectangle=((max_a[0]//100, max_a[1]//100),(max_b[0]//100, max_b[1]//100)))

    return max_area






if __name__ == "__main__":
    input_file_path = get_input_file_path(2025, 9)
    part_one(input_file_path)
    part_two(input_file_path)




# 4756718172
# 1665679194