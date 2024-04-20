from_n = []
from_s = []
from_l = []
from_o = []

cardeal_points = {"-1": from_o, "-2": from_s, "-3": from_n, "-4": from_l}

current_cardeal_point = None

fly_control = []

while True:
    entry = input()
    if entry == "0":
        break

    if entry in ["-1", "-2", "-3", "-4"]:
        current_cardeal_point = entry

    else:
        cardeal_points[current_cardeal_point].append(entry)

while from_n or from_s or from_l or from_o:
    if from_o:
        fly_control.append(from_o.pop(0))

    if from_n:
        fly_control.append(from_n.pop(0))

    if from_s:
        fly_control.append(from_s.pop(0))

    if from_l:
        fly_control.append(from_l.pop(0))

print(" ".join(fly_control))

