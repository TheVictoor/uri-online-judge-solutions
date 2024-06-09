import time
from collections import deque

start = time.time()

r, c = map(int, input().split())
image = [list(input()) for _ in range(r)]


def paint_blank_sequence(image, start, r, c):
    queue = deque([start])
    while queue:
        row, col = queue.popleft()  # BFS using queue
        if image[row][col] == ".":
            image[row][col] = "o"
            if col + 1 < c and image[row][col + 1] == ".":
                queue.append((row, col + 1))
            if col - 1 >= 0 and image[row][col - 1] == ".":
                queue.append((row, col - 1))
            if row + 1 < r and image[row + 1][col] == ".":
                queue.append((row + 1, col))
            if row - 1 >= 0 and image[row - 1][col] == ".":
                queue.append((row - 1, col))


paint_count = 0

for idxr in range(r):
    for idxc in range(c):
        if image[idxr][idxc] == ".":
            paint_blank_sequence(image, (idxr, idxc), r, c)
            paint_count += 1


print(paint_count)

end = time.time()
print(end - start)
