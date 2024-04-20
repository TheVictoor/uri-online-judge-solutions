n_tests = int(input())

for i in range(n_tests):
    tt = int(input())
    count = 0

    for ii in range(tt):
        count += 2**ii

    print(count)
