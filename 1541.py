import math

while 1:
	aaa = input()	
	inp = aaa.split(' ')
	if inp[0] == '0':
		break
	
	a = int(inp[0])
	b = int(inp[1])
	c = int(inp[2])

	mqdr = a * b
	x = (mqdr * 100) / c

	x = int(math.sqrt(x))

	print(x)
