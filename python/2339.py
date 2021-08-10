c, p, f = input().split()
c, p, f = int(c), int(p), int(f)

if p / c >= f:
  print("S")
else:
  print("N")