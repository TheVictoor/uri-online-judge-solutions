x = input()
x = x.split(' ')

i = input()
i = i.split(' ')

p = int(x[0])
cn = int(x[1])
g = 1
for y in range(1, cn):
 	a = int(i[y - 1])
 	b = int(i[y])
 	c = 0
 	if a > b:
 		c = a - b
 	elif a < b:
 		c = b - a

 	if c > p:
 		g = 0
 		break

if g == 1:
	print('YOU WIN')
elif g == 0:
	print('GAME OVER')