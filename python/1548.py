test_cases = int(input())

for i in range(test_cases):
    a = int(input())
    n = input().split(" ")
    n = [int(item) for item in n]
    nc = n.copy()
    n.sort(reverse=True)
    c = 0
    for [a, b] in zip(n, nc):
        if a == b:
            c += 1

    print(c)
