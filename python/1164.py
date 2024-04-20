x = int(input())

for i in range(x):
    n = int(input())
    s = 0
    for y in range(1, n):
        if n % y == 0:
            s += y

    if s == n:
        print("%d eh perfeito" % n)
    else:
        print("%d nao eh perfeito" % n)

