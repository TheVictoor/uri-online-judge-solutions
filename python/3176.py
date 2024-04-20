n = int(input())

by_age = {}
list_all = []

for i in range(n):
    name, age = input().split()
    by_age[age] = by_age.get(age, [])
    by_age.get(age, []).append(name)

keys = list(by_age.keys())
keys.sort()
keys.reverse()

for age in keys:
    names = by_age.get(age)
    if len(names) > 1:
        names.sort()

    list_all.extend(zip([age] * len(names), names))

teams = {}
n_teams = len(list_all) // 3
for f in range(3):
    for p in range(n_teams):
        teams[p + 1] = teams.get(p + 1, [])
        teams.get(p + 1, []).append(list_all.pop(0))

for team in teams.keys():
    print(f"Time {team}")
    members = teams.get(team)
    for age, name in members:
        print(f"{name} {age}")
    print()
