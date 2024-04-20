while 1:
    q = input()
    q = q.split()

    x = int(q[0])
    y = int(q[1])

    if x == 0 or y == 0:
        break

    if x > 0:
        if y > 0:
            print("primeiro")
        elif y < 0:
            print("quarto")
    elif x < 0:
        if y > 0:
            print("segundo")
        elif y < 0:
            print("terceiro")
