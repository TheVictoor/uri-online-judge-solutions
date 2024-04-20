n_tests = int(input())

for i in range(n_tests):
    n_shots = int(input())
    shots = input().split()
    actions = input()

    shots_hit = 0

    for i, shot in enumerate(shots):
        shot_height = int(shot)

        if shot_height > 2 and actions[i] == "J":
            shots_hit += 1

        if shot_height <= 2 and actions[i] == "S":
            shots_hit += 1

    print(shots_hit)
