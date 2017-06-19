n = int(input())

i = 0
b = 1
x = 0


for q in range(n):
	if q == 0:
		if q == n -1:
			print(i)
			continue
		else:
			print(i , end=' ')
			continue
	elif q == 1:
		if q == n -1:
			print(b)
			continue
		else:	
			print(b , end=' ')
			continue
	else:
		if q == n -1:
			x = i + b
			i = b
			b = x
			print(x)
			continue
		else:	
			x = i + b
			i = b
			b = x
			print(x , end=' ')
		


