while 1:
	try:
		#configura as variareis
		i = int(input())
		v = []
		ll = []

		#criar vetor com todos os valores zerados
		for l in range(i):
			ll = []
			for c in range(i):
				ll += [0]
			v.append(ll)

		#preencher a diagonal com 2
		for l in range(i):
			v[l][l] = 2

		#preencher a diagonal com 3
		for l in range(i):
			v[l][i - (l + 1)] = 3

		#preencher o centro com 1
		a = i // 3
		for l in range(a, i - a):
			for c in range(a , i - a):
				v[l][c] = 1

		#configura o valor central como 4
		vc = i // 2
		v[vc][vc] = 4

		#mostrar o vetor
		for l in range(i):
			for c in range(i):
				if c == i - 1:
					print(v[l][c])
				else:
					print(v[l][c], end='')
		print()
	except:
		break