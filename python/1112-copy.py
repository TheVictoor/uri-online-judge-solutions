class Query:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def updateBIT(bit,x, yy, val, X, Y):
    while x <= X:
        y = yy
        while y <= Y:
            bit[x][y] += val
            y += (y & -y)
        x += (x & -x)


def getSum(bit, x, yy):
    sum = 0
    while x > 0:
        y = yy 
        while y > 0:
            sum += bit[x][y]
            y -= y & -y
        x -= x & -x
    return sum


def answerQueries(q, bit):
    x1 = q.x1 + 1
    y1 = q.y1 + 1
    x2 = q.x2 + 1
    y2 = q.y2 + 1

    v1 = getSum(bit, x2, y2)
    v2 = getSum(bit, x2, y1 - 1)
    v3 = getSum(bit, x1 - 1, y2)
    v4 = getSum(bit, x1 - 1, y1 - 1)

    # print(v1, v2, v3, v4)

    return v1 - v2 - v3 + v4

while True:
    x, y, p = [int(x) for x in input().split(" ")]

    if x == y == p == 0:
        break

    q = int(input())

    bit = [None for i in range(x + 1)]
    for i in range(x + 1):
        bit[i] = [None for i in range(y + 1)]
        for j in range(y + 1):
            bit[i][j] = 0

    mat = [None for i in range(x)]
    for i in range(x):
        mat[i] = [None for i in range(y)]
        for j in range(y):
            mat[i][j] = 0

    for i in range(q):
        a = input()

        if a[0] == "A":
            _, an, ax, ay = a.split(" ")

            an = int(an)
            ii = int(ax)
            jj = int(ay)

            mat[ii][jj] += an

            updateBIT(bit, ii+1, jj+1, an, x, y)

        else:
            _, fx, fy, ux, uy = a.split(" ")

            fx = int(fx)
            fy = int(fy)
            ux = int(ux)
            uy = int(uy)

            x1, x2 = ux, fx
            if x2 < x1:
                x1, x2 = x2, x1

            y1, y2 = uy, fy
            if y2 < y1:
                y1, y2 = y2, y1

            q = Query(x1, y1, x2, y2)
            ans = answerQueries(q,  bit)

            print(ans * p)

