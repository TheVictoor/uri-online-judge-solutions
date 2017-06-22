while 1:
	try:
		q = int(input())
		l = input()
		l = l.split(' ')
		vm = 1
		for a in range(len(l)):
			if int(l[a]) < 10:
				vl = 1
			elif int(l[a]) < 20:
				vl = 2
			else:
				vl = 3
			if vl > vm:
				vm = vl
		print(vm)
	except:
		break