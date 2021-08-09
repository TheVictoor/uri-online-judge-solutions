p1, c1, p2, c2 = input().split()
p1, c1, p2, c2 = int(p1), int(c1), int(p2), int(c2)

p1r = p1*c1
p2r = p2*c2

if p1r == p2r:
  print(0)
elif p1r > p2r:
  print(-1)
else:
  print(1)