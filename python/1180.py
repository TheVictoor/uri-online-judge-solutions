a = int(input())
b = input()
v = b.split(" ")

f = 0
ff = len(v)

# remover os espaços em braco apos o tamanho determinado do vetor pela entrada da viariavel a
# ff = e o tamanho do vetor
# a = o tamanho que deveria ser o vetor
if ff != a:
    while 1:
        if v[f] == "":
            v.pop(f)
            f = 0
            ff = len(v)
        else:
            f += 1
            ff -= 1
        if ff == 0:
            break

mv = int(v[0])
ind = 0

for i in range(len(v)):
    x = int(v[i])
    if mv > x:
        mv = x
        ind = i

print("Menor valor: %d\nPosicao: %d" % (mv, ind))

