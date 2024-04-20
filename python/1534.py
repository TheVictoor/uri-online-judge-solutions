while 1:
    try:
        v = []
        li = []
        x = int(input())

        # cria e configura a matriz
        for l in range(x):
            li = []
            for c in range(x):
                li += [3]
            v.append(li)

        # configuras os valores 1 da matriz
        for l in range(x):
            v[l][l] = 1

        # configura os valores 2 da matriz
        for l in range(x):
            v[l][x - (l + 1)] = 2

        # mostra a matriz
        for l in range(x):
            for c in range(x):
                if c == x - 1:
                    print(v[l][c])
                else:
                    print(v[l][c], end="")

    except:
        break

