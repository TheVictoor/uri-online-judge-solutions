x = int(input())
z = int(input())
c = 1
while z <= x:
    z = int(input())

s = x
while 1:
    s += x + 1
    x += 1
    c += 1
    if s > z:
        break

print(c)

