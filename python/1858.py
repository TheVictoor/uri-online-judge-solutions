qn = int(input())
n = input()
n = n.split(" ")
mr = 0
v = 0

if int(n[0]) > int(n[1]):
    mr = 1
else:
    mr = 0

for i in range(1, len(n)):
    if int(n[i]) < int(n[mr]):
        mr = i
        v = int(n[i])

print(mr + 1)

