from collections import defaultdict

if __name__ == "__main__":
    r, c = map(int, input().split(" "))

    dag: dict[int, list[tuple[int, int]]] = defaultdict(list)

    for ci in range(c):
        a, b, p = map(int, input().split(" "))
        dag[a].append((b, p))
        dag[b].append((a, p))

    visited = set()
    visited.add(1)

    nexts: set[tuple[int, int]] = set()
    for i in dag[1]:
        nexts.add(i)

    current_tree = []

    while len(visited) != len(dag.keys()):
        # next node with min value
        next = min(nexts, key=lambda a: a[1])
        nexts.remove(next)

        # if this node was already visited, we discard this iteration
        if next[0] in visited:
            continue

        # we add all conected node to the list
        for i in dag[next[0]]:
            nexts.add(i)

        # since this node is the one with lower value,
        # we add it to the current_tree
        current_tree.append(next[1])

        # we mark this node as visited and
        # continue the iteration until visit all nodes
        visited.add(next[0])

    print(sum(current_tree))
