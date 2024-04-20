x = int(input())

s = 0
b = 0
a = 0

ts = 0
tb = 0
ta = 0

for i in range(x):
    n = input()

    t = input()
    t = t.split(" ")

    y = input()
    y = y.split(" ")

    ts += int(t[0])
    tb += int(t[1])
    ta += int(t[2])

    s += int(y[0])
    b += int(y[1])
    a += int(y[2])

print("Pontos de Saque: %.2f %%." % (s / ts * 100))
print("Pontos de Bloqueio: %.2f %%." % (b / tb * 100))
print("Pontos de Ataque: %.2f %%." % (a / ta * 100))

