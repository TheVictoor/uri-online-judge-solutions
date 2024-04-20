q = input()
q = q.split()

x = int(q[0])
y = int(q[1])

for i in range(1, y + 1):
    if i % x != 0:
        print(i, end=" ")
    elif i % x == 0:
        print(i)
