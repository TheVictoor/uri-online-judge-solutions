i = int(input())
f = int(input())
s = 0

if i > f:
	i,f = f,i

for x in range(i ,f+1):
	if x % 13 != 0:
		s += x

print(s)
