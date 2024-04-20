while 1:
    x = int(input())
    if x == 0:
        break

    for i in range(x):
        v = int(input())
        if v % 2 == 0:
            print(v * 2 - 2)
        else:
            print(v * 2 - 1)
