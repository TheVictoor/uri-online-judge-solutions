a = 1
while 1:
    try:
        sb = input()
        s = input()
        q = 0
        p = 0
        hit = 0

        h = len(s) - len(sb)

        for i in range(h + 1):
            hit = 0
            for z in range(len(sb)):
                if sb[z] == s[i + z]:
                    hit += 1
                    # print('hit = %d' %hit)
                else:
                    hit = 0
                    # print('hit = 0')

            # print('here 4')
            if hit == len(sb):
                q += 1
                p = i
                # print('quantidade %d pos %d' %(q, p))

        print("Caso #%d:" % a)
        if q == 0:
            print("Nao existe subsequencia")
        else:
            print("Qtd.Subsequencias: %d" % q)
            print("Pos: %d" % (p + 1))

        print()
        a += 1
    except:
        break

