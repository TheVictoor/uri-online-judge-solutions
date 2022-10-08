while 1:
    try:
        n = input()

        if n == 0:
            break

        list_of_values = input().split(' ')

        d = {}
        p = []

        for i in list_of_values:
            if i == '':
                continue
            if d.get(i):
                d[i] = d[i] + 1
            else:
                d[i] = 1

        for k, i in d.items():
            if i & 1 == 1:
                p.append(int(k))

        p.sort()
        print(*p)
    except:
        break