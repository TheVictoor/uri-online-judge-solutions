def check_train_sequence(desired_wagons_sequence: list, a_direction: list):
    station = []
    b_direction = []
    ok = True

    for d in desired_wagons_sequence:
        is_there = True if station and station[-1] == d else False

        if is_there:
            b_direction.append(d)
            station = station[:-1]
            continue

        while a_direction:
            a = a_direction[0]
            a_direction = a_direction[1:]
            if a == d:
                b_direction.append(d)
                break
            else:
                station.append(a)

        if b_direction[-1] != d:
            ok = False
            break

    return ok


while True:
    try:
        x = int(input())

        while 1:
            i = input()
            if i == "0":
                print()
                break
            i = i.split(" ")
            i = [int(a) for a in i]
            l = list(range(1, x + 1))
            print("Yes") if check_train_sequence(i, l) else print("No")
    except:
        break
