def retangulo(a, b, c):
	if a**2 + b ** 2 == c**2:
		print('Retangulo: S')
	else:
		print('Retangulo: N')


x = input()
x = x.split(' ')
a = int(x[0])
b = int(x[1])
c = int(x[2])

if a > b and a > c:
	a , c = c , a
elif b > a and b > c:
	b , c = c , b


if a == b and b == c and c + b > a and b + a > c and a + c > b:
  	print('Valido-Equilatero')
  	retangulo(a , b, c)
elif (a == b or b == c or c == a) and c + b > a and b + a > c and a + c > b:
	print('Valido-Isoceles')
	retangulo(a , b, c)
elif c + b > a and b + a > c and a + c > b:
	print('Valido-Escaleno')
	retangulo(a , b, c)
else:
	print('Invalido')
