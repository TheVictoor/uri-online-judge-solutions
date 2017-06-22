tp = input()

tp = tp.split(' ')

a = int(tp[0])
b = int(tp[1])
c = int(tp[2])


if a > b and ((b < c) or (c == b)):
	print(':)')
elif a < b and ((b == c) or (b > c)):
	print(':(')
elif a < b and b < c and (b - a) > (c - b):
	print(':(')
elif a < b and b < c and (c - b) >= (b - a):
	print(':)')
elif a > b and b > c and (a - b) > (b - c):
	print(':)')
elif a > b and b > c and (a - b) <= (b - c):
 	print(':(')
elif a == b and b < c:	
	print(':)')
elif a == b and b > c:
	print(':(')
else:
	print(':(')
