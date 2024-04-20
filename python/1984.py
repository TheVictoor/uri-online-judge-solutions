x = int(input())
x = str(x)
a = int(x)

# essa seria a solução mais simples
# print(x[::-1])

v = 0
# decompoe o valor e mostra
for i in range(len(x)):
    v = a % 10
    print(v, end="")
    a = a // 10

print()

