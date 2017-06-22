while 1:
	size = int(input())

	if size == 0:
		break

	v = []
	linha = []

	for lin in range(size):
		linha = []
		d = 1
		for col in range(1, size+1):
			if col == 1:
				linha += [1]
			else:
				linha += [d * 2]
				d *= 2
		v.append(linha)

	for lin in range(1, size):
		for col in range(size):
			v[lin][col] = v[lin-1][col] * 2



	cf = int(len(str(v[size-1][size-1])))
	
	for lin in range(size):
		for col in range(size):
			if cf == 1:
				if size == 1:
					print('%1d' %v[lin][col])
				elif col == 0:
					print('%1d' %v[lin][col], end='')
				elif col == size - 1:
					print(' %1d' %v[lin][col])				
				else:
					print(' %1d' %v[lin][col], end='')
			elif cf == 2:
				if col == 0:
					print('%2d' %v[lin][col], end='')
				elif col == size - 1:
					print(' %2d' %v[lin][col])				
				else:
					print(' %2d' %v[lin][col], end='')
			elif cf == 3:
				if col == 0:
					print('%3d' %v[lin][col], end='')
				elif col == size - 1:
					print(' %3d' %v[lin][col])				
				else:
					print(' %3d' %v[lin][col], end='')
			elif cf == 4:
				if col == 0:
					print('%4d' %v[lin][col], end='')
				elif col == size - 1:
					print(' %4d' %v[lin][col])				
				else:
					print(' %4d' %v[lin][col], end='')

			elif cf == 5:
				if col == 0:
					print('%5d' %v[lin][col], end='')
				elif col == size - 1:
					print(' %5d' %v[lin][col])				
				else:
					print(' %5d' %v[lin][col], end='')
			elif cf == 6:
				if col == 0:
					print('%6d' %v[lin][col], end='')
				elif col == size - 1:
					print(' %6d' %v[lin][col])				
				else:
					print(' %6d' %v[lin][col], end='')

			elif cf == 7:
				if col == 0:
					print('%7d' %v[lin][col], end='')
				elif col == size - 1:
					print(' %7d' %v[lin][col])				
				else:
					print(' %7d' %v[lin][col], end='')

			elif cf == 8:
				if col == 0:
					print('%8d' %v[lin][col], end='')
				elif col == size - 1:
					print(' %8d' %v[lin][col])				
				else:
					print(' %8d' %v[lin][col], end='')
			elif cf == 9:
				if col == 0:
					print('%9d' %v[lin][col], end='')
				elif col == size - 1:
					print(' %9d' %v[lin][col])				
				else:
					print(' %9d' %v[lin][col], end='')

			elif cf == 10:
				if col == 0:
					print('%10d' %v[lin][col], end='')
				elif col == size - 1:
					print(' %10d' %v[lin][col])				
				else:
					print(' %10d' %v[lin][col], end='')
	print()