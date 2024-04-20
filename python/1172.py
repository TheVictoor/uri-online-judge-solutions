lista = []

for i in range(10):
    x = int(input())
    lista += [x]

for a in range(10):
    if lista[a] <= 0:
        lista[a] = 1

for z in range(10):
    print("X[%d] = %d" % (z, lista[z]))

