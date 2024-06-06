def get_nexts(
    matrix: list[list[str]],
    current: tuple[int, int],
    visited: set[tuple[int, int]],
) -> list[tuple[int, int]]:
    nexts = []

    if current[1] + 1 < 5:
        nexts.append((current[0], current[1] + 1))

    if current[0] + 1 < 5:
        nexts.append((current[0] + 1, current[1]))

    if current[1] - 1 >= 0:
        nexts.append((current[0], current[1] - 1))

    if current[0] - 1 >= 0:
        nexts.append((current[0] - 1, current[1]))

    # print(nexts)
    # print(matrix)

    return list([n for n in nexts if n not in visited and matrix[n[0]][n[1]] != "1"])


def dfs(
    matrix: list[list[str]],
    visited: set[tuple[int, int]],
    current: tuple[int, int],
    target: tuple[int, int],
):
    if current == targed:
        return True

    visited.add(current)

    next_moves = get_nexts(matrix, current, visited)

    for n in next_moves:
        r = dfs(matrix, visited, n, target)
        if r:
            return r

    return False


n_tests = int(input())

for i in range(n_tests):
    # always 5x5
    # filled with 0 and 1
    matrix = []

    visited = set()
    current = (0, 0)
    targed = (4, 4)

    c = 0
    while c < 5:
        i = input().strip()
        if len(i):
            matrix.append(i.split(" "))
            c += 1

    if matrix[current[0]][current[1]] == "0":
        r = dfs(matrix, visited, current, targed)
    else:
        r = False

    print("COPS" if r else "ROBBERS")
