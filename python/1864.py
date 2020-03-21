x = int(input())
s = 'LIFE IS NOT A PROBLEM TO BE SOLVED'

for i in range(x):
	if i == x - 1:
		print(s[i])
	else:
		print(s[i], end='')
