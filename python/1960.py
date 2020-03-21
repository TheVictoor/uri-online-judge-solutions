
x = int(input())

if len(str(x)) == 4:
	print('M')

elif len(str(x)) == 3:

	a = x % 10
	x = x // 10
	b = x % 10
	x = x // 10
	c = x 
	if c == 9:
		print('CM' , end='')
	elif c == 8:
		print('DCCC', end='')
	elif c == 7:
		print('DCC', end='')
	elif c == 6:
		print('DC', end='')
	elif c == 5:
		print('D', end='')
	elif c == 4:
		print('CD', end='')
	elif c == 3:
		print('CCC', end='')
	elif c == 2:
		print('CC', end='')
	elif c == 1:
		print('C', end='')

	if b == 0:
		print('' , end='')
	elif b == 9:
		print('XC' , end='')
	elif b == 8:
		print('LXXX', end='')
	elif b == 7:
		print('LXX', end='')
	elif b == 6:
		print('LX', end='')
	elif b == 5:
		print('L', end='')
	elif b == 4:
		print('XL', end='')
	elif b == 3:
		print('XXX', end='')
	elif b == 2:
		print('XX', end='')
	elif b == 1:
		print('X', end='')

	if a == 0:
		print()
	elif a == 9:
		print('IX')
	elif a == 8:
		print('VIII')
	elif a == 7:
		print('VII')
	elif a == 6:
		print('VI')
	elif a == 5:
		print('V')
	elif a == 4:
		print('IV')
	elif a == 3:
		print('III')
	elif a == 2:
		print('II')
	elif a == 1:
		print('I')


elif len(str(x)) == 2:
	a = x % 10
	x = x // 10
	b = x 

	if b == 9:
		print('XC' , end='')
	elif b == 8:
		print('LXXX', end='')
	elif b == 7:
		print('LXX', end='')
	elif b == 6:
		print('LX', end='')
	elif b == 5:
		print('L', end='')
	elif b == 4:
		print('XL', end='')
	elif b == 3:
		print('XXX', end='')
	elif b == 2:
		print('XX', end='')
	elif b == 1:
		print('X', end='')

	if a == 0:
		print()
	elif a == 9:
		print('IX' )
	elif a == 8:
		print('VIII')
	elif a == 7:
		print('VII')
	elif a == 6:
		print('VI')
	elif a == 5:
		print('V')
	elif a == 4:
		print('IV')
	elif a == 3:
		print('III')
	elif a == 2:
		print('II')
	elif a == 1:
		print('I')
else:
	a = x

	if a == 9:
		print('IX' )
	elif a == 8:
		print('VIII')
	elif a == 7:
		print('VII')
	elif a == 6:
		print('VI')
	elif a == 5:
		print('V')
	elif a == 4:
		print('IV')
	elif a == 3:
		print('III')
	elif a == 2:
		print('II')
	elif a == 1:
		print('I')
