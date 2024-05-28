ntests = int(input())
input()

trees = {}
total = 0

while ntests >= 1:
    try:
        tree = input()

        if tree == "":
            keys = list(trees.keys())
            keys.sort()

            for k in keys:
                print("%s %.4f" % (k, trees[k] * 100 / total))
            print("")

            trees = {}
            total = 0
            ntests -= 1

            continue

        if tree in trees:
            trees[tree] += 1
            total += 1
        else:
            trees[tree] = 1
            total += 1

    except Exception:
        break


keys = list(trees.keys())
keys.sort()
for k in keys:
    print("%s %.4f" % (k, trees[k] * 100 / total))
