ci = 0
cp = 0
i = [1,1,1,1,1]
p = [0,0,0,0,0]

for x in range(15):
	v = int(input())
	if v % 2 == 0:
		p[cp] = v
		cp += 1
		if cp == 5:
			for b in range(cp):
				print('par[%d] = %d' %( b , p[b]))
			cp = 0
	else:
		i[ci] = v
		ci += 1
		if ci == 5:
			for a in range(ci):
				print('impar[%d] = %d' %(a , i[a]))
			ci = 0

for c in range(ci):
	print('impar[%d] = %d' %(c , i[c]))

for b in range(cp):
	print('par[%d] = %d' %( b , p[b]))


