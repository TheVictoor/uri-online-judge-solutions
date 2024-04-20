while 1:
    size = int(input())
    if size == 0:
        break
    mat = []
    linha = []

    # cria uma matriz SIZExSIZE e configura seus valores para 1
    for i in range(size):
        linha = []
        for c in range(size):
            linha += [1]
        mat.append(linha)

    if size / 2 > size // 2:
        ctr = size // 2 + 1
    else:
        ctr = size // 2

    for cn in range(1, ctr + 1):
        # para testes
        # print('camada %d' %cn)
        for lin in range(cn - 1, size - (cn - 1)):
            # para testes
            # print('\tlinha %d' %lin)
            for col in range(cn - 1, size - (cn - 1)):
                # para teste
                # print('\t\tcoluna %d'%col)
                mat[lin][col] = cn

    # mostra matriz
    for i in range(size):
        for c in range(size):
            if c == 0 and size == 1:
                print("%3d" % mat[i][c])
            elif c == 0:
                print("%3d" % mat[i][c], end="")
            elif c == size - 1:
                print(" %3d" % mat[i][c])
            else:
                print(" %3d" % mat[i][c], end="")
    print()
