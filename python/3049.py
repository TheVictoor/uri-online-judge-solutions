b = int(input())
t = int(input())

a = 70
base = 160
top = 160

side_a = b + t
side_b = (base - b) + (top - t)

if side_a > side_b:
    print(1)
elif side_a < side_b:
    print(2)
else:
    print(0)
