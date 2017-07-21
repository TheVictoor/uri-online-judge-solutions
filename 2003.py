while 1:
	try:
		h = input()
		h = h.split(':')

		hmax = int(h[0]) + 1
		mmax = int(h[1])

		hh = hmax - 8

		if hh < 0:
			print('Atraso maximo: 0')
		else:
			mmax += 60 * hh
			print('Atraso maximo: %d' %mmax)
	except:
		break