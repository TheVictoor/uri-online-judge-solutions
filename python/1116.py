n = int(input())

for i in range(n):
    q = input()
    q = q.split(" ")

    n = int(q[0])
    m = int(q[1])

    try:
        d = n / m
        print("%.1f" % d)
    except:
        print("divisao impossivel")

