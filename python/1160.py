c = int(input())

for i in range(c):
    q = input()
    q = q.split(" ")
    pa = int(q[0])
    pb = int(q[1])
    ga = float(q[2])
    gb = float(q[3])
    ano = 0
    while pa <= pb:
        pa += (pa * ga) // 100
        pb += (pb * gb) // 100
        ano += 1
        if ano > 100:
            print("Mais de 1 seculo.")
            break

    if ano > 100:
        continue
    else:
        print("%d anos." % ano)
