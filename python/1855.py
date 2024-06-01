from collections import defaultdict

c = int(input())
r = int(input())

map = []

for idx in range(r):
    map.append(list(input()))

visited = defaultdict(int)

direction = ""
current: tuple[int, int] = (0, 0)


def current_p(map, curr):
    return map[curr[0]][curr[1]]


while not visited[str(current)] and current_p(map, current) != "*":
    visited[str(current)] = 1
    if current_p(map, current) in [">", "<", "v", "^"]:
        direction = current_p(map, current)

    if direction == ">":
        if current[1] + 1 >= c:
            break
        current = [current[0], current[1] + 1]
    elif direction == "<":
        if current[1] - 1 < 0:
            break
        current = [current[0], current[1] - 1]
    elif direction == "v":
        if current[0] + 1 >= r:
            break
        current = [current[0] + 1, current[1]]
    elif direction == "^":
        if current[0] - 1 < 0:
            break
        current = [current[0] - 1, current[1]]

if current_p(map, current) != "*":
    print("!")
else:
    print("*")
