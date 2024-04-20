while True:
    x = input()
    if x == "0":
        break

    q = 0
    for i in range(int(x)):
        q += (i + 1) * (i + 1)
    print(q)

