a = input()
a = a.split(" ")

x = int(a[0])
b = int(a[1])
c = 2


s = 0

while b < 0 or b == 0:
    b = int(a[c])
    c += 1

for i in range(b):
    s += i + x

print(s)

