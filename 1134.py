#1.Álcool 2.Gasolina 3.Diesel 
di = 0
al = 0
ga = 0

while 1:
	c = int(input())

	if c < 1 or c > 4:
		continue
	elif c == 4:
		break
	elif c == 3:
		di += 1
	elif c == 2:
		ga += 1
	elif c == 1:
		al += 1

print('MUITO OBRIGADO')
print('Alcool: %d' %al)
print('Gasolina: %d' %ga)
print('Diesel: %d' %di)
