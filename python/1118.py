while 1:
    n1 = float(input())
    n2 = float(input())

    while n1 < 0 or n1 > 10:
        print("nota invalida")
        n1 = float(input())

    while n2 > 10 or n2 < 0:
        print("nota invalida")
        n2 = float(input())

    m = (n1 + n2) / 2
    print("media = %.2f" % m)

    while 1:
        print("novo calculo (1-sim 2-nao)")
        k = int(input())
        if k == 1 or k == 2:
            break

    if k == 2:
        break
