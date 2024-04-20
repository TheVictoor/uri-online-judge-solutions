while True:
    x = int(input())
    if x == 0:
        break

    n = 0
    for i in range(x):
        n += (x - i) ** 2

    print(n)

