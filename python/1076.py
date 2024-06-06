from collections import defaultdict


def bfs(
    parent,
    visited: set[str],
    current: str,
    start: str,
    total: int,
    dag: list[list[str]],
):
    visited.add(current)
    if current == start and len(visited) == total:
        return 0

    c = 2 if parent is not None else 0
    nexts = list(dag[current])
    for n in nexts:
        # to avoid cyclic we do not traverse to the parent
        if n != parent:
            c += bfs(current, visited, n, start, total, dag)

    return c


n_tests = int(input())

for test in range(n_tests):
    start = input()
    v, a = map(int, input().split(" "))

    dag = defaultdict(set)

    for ia in range(a):
        a, b = input().split(" ")
        dag[a].add(b)
        dag[b].add(a)

    c = bfs(None, set(), start, start, len(dag.keys()), dag)

    print(c)
