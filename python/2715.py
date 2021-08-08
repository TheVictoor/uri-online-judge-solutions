import math

while True:
	try:
		n = int(input())
		current_count = 0
		entries = [int(e) for e in input().split()]

		indice = len(entries) // 2
		diff = math.inf

		entries_v2 = []
		current_count = 0
		for i in entries:
			current_count += i
			entries_v2.append(current_count)

		list_in_use = entries_v2.copy()

		while list_in_use:
			if indice == 0:
				break

			left = list_in_use[:indice]
			right = list_in_use[indice:] 
			rangel = left[-1]
			gugu = entries_v2[-1]
			current_diff = rangel - (gugu - rangel)

			if abs(current_diff) < abs(diff):
				diff = current_diff
			
			if current_diff < 0:
				list_in_use = right
				indice = len(right) // 2
			elif current_diff > 0:
				list_in_use = left
				indice = len(left) // 2

			if diff == 0:
				break

		print(abs(diff))
	except EOFError:
		break

