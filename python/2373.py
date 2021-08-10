n_trays = int(input())
broken_cups = 0

for i in range(n_trays):
  cans, cups = input().split()
  cans, cups = int(cans), int(cups)
  if cans > cups:
    broken_cups += cups  

print(broken_cups)