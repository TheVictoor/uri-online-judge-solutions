x = int(input())

fib = [0, 1]
a = 0
b = 1

for i in range(2, 61):
    fib += [a + b]
    a = b
    b = fib[i]


for i in range(x):
    v = int(input())
    print("Fib(%d) = %d" % (v, fib[v]))
