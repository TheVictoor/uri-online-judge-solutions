n = 0
vi = 0
vg = 0
e = 0

while 1:
	q = input()
	q = q.split(' ')

	gi = int(q[0])
	gg = int(q[1])

	if gi > gg:
		vi+= 1
	elif gg > gi:
		vg+= 1
	elif gg == gi:
		e+= 1

	n+= 1

	print('Novo grenal (1-sim 2-nao)')
	x = int(input())
	if x == 2:
		break

print('%d grenais' %n)
print('Inter:%d' %vi)
print('Gremio:%d' %vg)
print('Empates:%d' %e)
if vi > vg: 
	print('Inter venceu mais')
elif vg > vi:
	print('Gremio venceu mais')

