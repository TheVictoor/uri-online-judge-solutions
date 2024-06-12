import sys
import time
from collections import defaultdict

start = time.time()

sys.setrecursionlimit(100000)


def preprocess_LCA(n, adj, root):
    MAX_LOG = 16
    parent = [[-1] * (MAX_LOG + 1) for _ in range(n + 1)]
    depth = [0] * (n + 1)
    dist = [0] * (n + 1)

    def dfs(v, p, d):
        parent[v][0] = p
        depth[v] = d
        for u, w in adj[v]:
            if u != p:
                dist[u] = dist[v] + 1
                dfs(u, v, d + 1)

    # Initialize parent and depth
    dfs(root, -1, 0)

    # Binary lifting
    for k in range(1, MAX_LOG + 1):
        for v in range(1, n + 1):
            if parent[v][k - 1] != -1:
                parent[v][k] = parent[parent[v][k - 1]][k - 1]

    return parent, depth, dist


def LCA(u, v, parent, depth):
    if depth[u] < depth[v]:
        u, v = v, u
    MAX_LOG = len(parent[0]) - 1

    # Lift u to the same depth as v
    for k in range(MAX_LOG, -1, -1):
        if depth[u] - (1 << k) >= depth[v]:
            u = parent[u][k]

    if u == v:
        return u

    # Lift u and v together
    for k in range(MAX_LOG, -1, -1):
        if parent[u][k] != parent[v][k]:
            u = parent[u][k]
            v = parent[v][k]

    return parent[u][0]


def calculate_distances(n, cards, adj):
    root = 1
    parent, depth, dist = preprocess_LCA(n, adj, root)

    card_positions = defaultdict(list)
    for i in range(1, n + 1):
        card_positions[cards[i - 1]].append(i)

    total_points = 0

    for positions in card_positions.values():
        if len(positions) == 2:
            u, v = positions
            lca = LCA(u, v, parent, depth)
            distance = dist[u] + dist[v] - 2 * dist[lca]
            total_points += distance

    return total_points


def main():
    input = sys.stdin.read
    data = input().split()

    idx = 0
    N = int(data[idx])
    idx += 1

    cards = [int(data[i]) for i in range(idx, idx + N)]
    idx += N

    adj = defaultdict(list)
    for _ in range(N - 1):
        A = int(data[idx])
        B = int(data[idx + 1])
        adj[A].append((B, 1))
        adj[B].append((A, 1))
        idx += 2

    result = calculate_distances(N, cards, adj)
    print(result)


main()

end = time.time()
print(end - start)
