import sys

# import time
from collections import defaultdict

sys.setrecursionlimit(100000)
# start = time.time()

# Read input
input = sys.stdin.read
data = input().split()

# Initialize variables
ridx = 0
nCards = int(data[ridx])
ridx += 1
cards = [int(data[i]) for i in range(ridx, ridx + nCards)]
ridx += nCards

# Build the graph (DAG)
dag = defaultdict(list)
for _ in range(nCards - 1):
    A = int(data[ridx])
    B = int(data[ridx + 1])
    dag[A - 1].append(B - 1)
    dag[B - 1].append(A - 1)
    ridx += 2

# Helper dictionaries to track distances and card sequences
distances = defaultdict(lambda: int(-1))
calculating_distances = defaultdict(list)
start_idx = 0
visited = set([start_idx])
calculating_distances[cards[start_idx]] = ["0"]

# Initialize total distance
total = 0


# Depth-First Search (DFS) function
def dfs(idx, n, cards_seq):
    global total
    visited.add(idx)
    current_card = cards[idx]
    if len(calculating_distances[current_card]) == 1:
        calculating_distances[current_card].append(cards_seq)

        a = calculating_distances[current_card][0]
        b = calculating_distances[current_card][1]

        i = 0
        while i < len(a) and i < len(b):
            if a[i] != b[i]:
                break
            i += 1

        i -= 1

        if i > 0:
            a = a[i:]
            b = b[i:]

        total += len(a) + len(b) - 2

    if len(calculating_distances[current_card]) == 0:
        calculating_distances[current_card].append(cards_seq)

    for next_idx in dag[idx]:
        if next_idx not in visited:
            dfs(next_idx, n + 1, cards_seq + [str(next_idx)])


# Start DFS from the start index
for i in dag[start_idx]:
    if i not in visited:
        dfs(i, 1, ["0", str(i)])

# Output the total distance
print(total)

# end = time.time()
# print(end - start)
