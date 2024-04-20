va = []
vb = []
vr = []
sa = ""
sb = ""
sr = ""

i = input()

i = i.split(" ")

a = i[0]
op = i[1]
b = i[2]


# decompondo valor e criando um vetor para fazer a substituição
x = int(a)
for i in range(len(a)):
    va.insert(0, x % 10)
    x //= 10

x = int(b)
for i in range(len(b)):
    # vb += [x % 10]
    vb.insert(0, x % 10)
    x //= 10

# percorrendo os vetores e subtituindo 7 por 0
for i in range(len(va)):
    if va[i] == 7:
        va[i] = 0

for i in range(len(vb)):
    if vb[i] == 7:
        vb[i] = 0

# transformando vetor em string
for i in range(len(va)):
    sa += str(va[i])

for i in range(len(vb)):
    sb += str(vb[i])

# convertento para inteiros
a = int(sa)
b = int(sb)

# fazendo operacao
if op == "+":
    r = a + b
elif op == "x":
    r = a * b

# transforma resposta em vetor

x = r
r = str(r)
for i in range(len(r)):
    vr.insert(0, x % 10)
    x //= 10

for i in range(len(vr)):
    if vr[i] == 7:
        vr[i] = 0

for i in range(len(vr)):
    sr += str(vr[i])

print(int(sr))

