x = int(input())

for i in range(x):
    n = int(input())
    s = 0
    for y in range(1, n + 1):
        if n % y == 0:
            s += 1

        if s >= 3:
            break

    if s == 2:
        print("%d eh primo" % n)
    else:
        print("%d nao eh primo" % n)

