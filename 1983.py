x = int(input())

m = 0
n = 0.0

for i in range(x):
	a = input()
	a = a.split(' ')
	b = float(a[1])

	if b > n:
		n = b
		m = int(a[0])

if n < 8.0:
	print('Minimum note not reached')
else:
	print(m)
