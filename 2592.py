while 1:
	i = int(input())
	if i == 0:
		break
	vp = []
	
	for i in range(1,i+1):
		vp += [str(i)]

	qq = 0
	while 1:
		q = input()
		q = q.split(' ')
		c = 0
		qq += 1

		for a in range(i):
			if vp[a] == q[a]:
				c += 1
		
		if c == len(vp) and c == len(q):
			break

	print(qq)