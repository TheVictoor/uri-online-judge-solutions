time_boundary, n_people = input().split()
time_boundary, n_people = int(time_boundary), int(n_people)

d = []

for i in range(n_people):
    time, person_name = input().split()
    hour, minute = time.split(":")
    if hour == "23":
        d.append((-(60 - int(minute)), person_name))
    else:
        d.append((int(minute), person_name))


d.sort(key=lambda x: x[0])


def apply_filter(v):
    if abs(v[0]) <= int(time_boundary):
        return True


d = list(filter(apply_filter, d))

[print(name) for time, name in d]
