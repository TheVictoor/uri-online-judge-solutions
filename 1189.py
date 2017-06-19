mat = [[0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0]]

op  = input()
cc = 0
s = 0

for l in range(12):
	for c in range(12):
		mat[l][c] = float(input())

#para fins de teste
#
#for l in range(1,11):
#	if l > 5:
#		for c  in range(11-l):
#			mat[l][c] = 1
#	else:
#		for c in range(l):
#			mat[l][c] = 1

if op == 'S':
	for l in range(1,11):
		if l > 5:
			for c  in range(11 - l):
				s += mat[l][c]
		else:
			for c in range(l):
				s += mat[l][c]
	print('%.1f' %s)

elif op == 'M':
	for l in range(1,11):
		if l > 5:
			for c  in range(11 - l):
				s += mat[l][c]
				cc += 1
		else:
			for c in range(l):
				s += mat[l][c]
				cc += 1
	m = s / cc
	print('%.1f' %m)