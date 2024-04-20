x = int(input())

for i in range(x):
    b = int(input())

    d = input()
    d = d.split(" ")

    g = input()
    g = g.split(" ")

    va = (int(d[0]) + int(d[1])) / 2

    vb = (int(g[0]) + int(g[1])) / 2

    if int(d[2]) % 2 == 0:
        va += b
    if int(g[2]) % 2 == 0:
        vb += b

    if va > vb:
        print("Dabriel")
    elif vb > va:
        print("Guarte")
    elif vb == va:
        print("Empate")
