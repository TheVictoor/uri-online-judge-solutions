mat = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

op = input()
cc = 0
s = 0

for l in range(12):
    for c in range(12):
        mat[l][c] = float(input())


if op == "S":
    for l in range(12):
        if l < 6:
            for c in range(11, 11 - l, -1):
                s += mat[l][c]
        else:
            for c in range(l + 1, 12):
                s += mat[l][c]
    print("%.1f" % s)

elif op == "M":
    for l in range(12):
        if l < 6:
            for c in range(11, 11 - l, -1):
                s += mat[l][c]
                cc += 1
        else:
            for c in range(l + 1, 12):
                s += mat[l][c]
                cc += 1
    m = s / cc
    print("%.1f" % m)

