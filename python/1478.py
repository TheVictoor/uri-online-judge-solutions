while 1:
    size = int(input())
    if size == 0:
        break

    v = []
    linha = []

    # cria matrz SIZExSIZE
    for lin in range(size):
        linha = []
        for col in range(size):
            linha += [1]
        v.append(linha)

    # configura os valores da matriz
    # parte diagonal superior
    for lin in range(size):
        cc = 1
        for col in range(lin, size):
            v[lin][col] = cc
            cc += 1

    # parte diagonal inferior
    for col in range(size):
        cc = 1
        for lin in range(col, size):
            v[lin][col] = cc
            cc += 1

    # mostra a matriz
    for l in range(size):
        for c in range(size):
            if size == 1:
                print("%3d" % v[l][c])
            elif c == size - 1:
                print(" %3d" % v[l][c])
            elif c == 0:
                print("%3d" % v[l][c], end="")
            else:
                print(" %3d" % v[l][c], end="")

    print()
