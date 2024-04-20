import math

while 1:
    try:
        x = input()
        x = x.split(" ")
        x1 = int(x[0])
        y1 = int(x[1])
        x2 = int(x[2])
        y2 = int(x[3])
        v = int(x[4])
        r1 = int(x[5])
        r2 = int(x[6])

        # distancia entre 2 pontos
        dab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # soma a distancia a quantidade de metros percorrida pelo adversario em um intervalo de 1.5 segundos
        dab += v * 1.5

        # raio de ação do ataque
        ra = r1 + r2

        if dab > float(ra):
            print("N")
        else:
            print("Y")
    except:
        break
