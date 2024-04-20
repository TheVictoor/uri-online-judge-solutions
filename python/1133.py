x = int(input())
y = int(input())

if x > y:
    x, y = y, x

for a in range(x + 1, y):
    if a % 5 == 2 or a % 5 == 3:
        print(a)
