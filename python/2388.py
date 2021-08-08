n_tests = int(input())

total_travel_km = 0

for i in range(n_tests):
	travel_time, velocity = input().split()
	travel_time, velocity = int(travel_time), int(velocity)
	total_travel_km += travel_time * velocity

print(total_travel_km)

