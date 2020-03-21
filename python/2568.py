i = input()

i = i.split(' ')

di = int(i[0])
va = int(i[1])
vr = int(i[2])
qd = int(i[3])
xx = di + qd

if di % 2 == 0 and xx % 2 == 0:
	print(va)
elif di % 2 == 1 and xx % 2 == 1:
	print(va)
elif di % 2 == 0 and xx % 2 == 1:
	print(va - vr)
elif di % 2 == 1 and xx % 2 == 0:
	print(va + vr)