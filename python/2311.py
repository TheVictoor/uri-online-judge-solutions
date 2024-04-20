x = int(input())

for i in range(x):
    nome = input()
    peso = float(input())
    n = input()
    notas = n.split(" ")
    media = 0.0

    for y in range(7):
        for j in range(6):
            if float(notas[j]) > float(notas[j + 1]):
                notas[j], notas[j + 1] = notas[j + 1], notas[j]

    for y in range(1, 6):
        media += float(notas[y])

    media *= peso

    print("%s %.2f" % (nome, media))

