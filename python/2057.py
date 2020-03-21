x = input()
x = x.split(' ')
p = int(x[0])
t = int(x[1])
f = int(x[2])
h = p + t + f

if h >= 24:
	h -= 24
elif h < 0:
	h += 24

print(h)