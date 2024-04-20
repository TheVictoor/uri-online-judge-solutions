n = int(input())
v = []
for i in range(n + 1):
    x = input()
    x = x.split(" ")
    v.append(x)

a = 0
for i in range(n):
    for j in range(n):
        if int(v[i][j]) == 1:
            a += 1
        if int(v[i][j + 1]) == 1:
            a += 1
        if int(v[i + 1][j]) == 1:
            a += 1
        if int(v[i + 1][j + 1]) == 1:
            a += 1

        if a >= 2:
            print("S", end="")
        else:
            print("U", end="")

        a = 0
    print()
