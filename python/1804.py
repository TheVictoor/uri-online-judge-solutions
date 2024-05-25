import time

start = time.time()

buggies = int(input())
list_buggies = list(map(int, input().split()))

bit = [0] * (buggies + 1)
len_bit = len(bit)


def update_bit(bit, idx, delta):
    while idx < len_bit:
        bit[idx] += delta
        idx += idx & (-idx)


def get_sum_bit(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s


for idx, value in enumerate(list_buggies):
    update_bit(bit, idx + 1, value)

while True:
    try:
        a, idx = input().split()
        idx = int(idx)
        if a == '?':
            s = get_sum_bit(bit, idx - 1)
            print(s)
        elif a == 'a':
            p = list_buggies[idx - 1]
            update_bit(bit, idx, -p)
    except Exception:
        break

end = time.time()
print(end - start)
