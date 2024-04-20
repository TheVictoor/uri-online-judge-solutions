a = int(input())

for i in range(a):
    b = int(input())

    if b >= 2015:
        b += 1
        c = b - 2015
        print("%d A.C." % c)
    else:
        c = 2015 - b
        print("%d D.C." % c)
