def get_next_values(
    size: int, l: int, c: int, v: int, visited: dict[tuple[int, int, int], bool]
):
    if l - 1 >= 0 and not visited.get((l - 1, c)):
        visited[(l - 1, c)] = True
        yield l - 1, c, v

    if c - 1 >= 0 and not visited.get((l, c - 1)):
        visited[(l, c - 1)] = True
        yield l, c - 1, v

    if l + 1 < size and not visited.get((l + 1, c)):
        visited[(l + 1, c)] = True
        yield l + 1, c, v

    if c + 1 < size and not visited.get((l, c + 1)):
        visited[(l, c + 1)] = True
        yield l, c + 1, v

    if l - 1 >= 0 and c - 1 >= 0 and not visited.get((l - 1, c - 1)):
        visited[(l - 1, c - 1)] = True
        yield l - 1, c - 1, v

    if l + 1 < size and c - 1 >= 0 and not visited.get((l + 1, c - 1)):
        visited[(l + 1, c - 1)] = True
        yield l + 1, c - 1, v

    if l - 1 >= 0 and c + 1 < size and not visited.get((l - 1, c + 1)):
        visited[(l - 1, c + 1)] = True
        yield l - 1, c + 1, v

    if l + 1 < size and c + 1 < size and not visited.get((l + 1, c + 1)):
        visited[(l + 1, c + 1)] = True
        yield l + 1, c + 1, v

    pass


def draw_m(m: list[list[int]]):
    for i in m:
        for d in i:
            print("%3d" % d, end="")
        print("\n")


def draw(size):
    m = [[0] * size for _ in range(size)]

    if size & 1 == 0:
        center_value = size // 2
    else:
        center_value = size // 2 + 1

    visited: dict[tuple[int, int], bool] = {}
    items: list[tuple[int, int, int]] = []

    if size & 1 != 0:
        # for odd numbers we have 1 value in the middle
        items.append((center_value - 1, center_value - 1, center_value))
        visited[(center_value - 1, center_value - 1)] = True
    else:
        # for even numbers we have the 4 values in middle
        items.append((center_value - 1, center_value - 1, center_value))
        items.append((center_value - 1, center_value, center_value))
        items.append((center_value, center_value - 1, center_value))
        items.append((center_value, center_value, center_value))
        visited[(center_value - 1, center_value - 1)] = True
        visited[(center_value - 1, center_value)] = True
        visited[(center_value, center_value - 1)] = True
        visited[(center_value, center_value)] = True

    while items:
        l, c, v = items.pop(0)
        m[l][c] = v
        n_items = list(get_next_values(size, l, c, v - 1, visited))
        items.extend(n_items)

    draw_m(m)


if __name__ == "__main__":
    draw(19)
