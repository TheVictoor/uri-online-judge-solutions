THRESHOLD = 40_000_000

telescope_area_in_mm = int(input())

seeable_stars = 0

n_stars = int(input())

for i in range(n_stars):
    if int(input()) * telescope_area_in_mm >= THRESHOLD:
        seeable_stars += 1

print(seeable_stars)

