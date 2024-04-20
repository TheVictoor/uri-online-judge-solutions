import math

while True:
    a, b, c = input().split()
    if a == b == c == "0":
        break
    print(math.floor((int(a) * int(b) * int(c)) ** (1 / 3)))

