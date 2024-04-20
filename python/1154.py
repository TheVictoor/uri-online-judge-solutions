a = 0
c = 0
while 1:
    i = int(input())
    if i < 0:
        break
    else:
        a += i
        c += 1

print("%.2f" % (a / c))

