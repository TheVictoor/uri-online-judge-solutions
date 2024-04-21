def generate_primes():
    primes = [2]
    primes_map = {1: True, 2: True}
    max_prime = 100000

    current_prime = 3
    while len(primes) < 3501:
        if current_prime & 1 != 0 and primes_map.get(current_prime) is not False:
            primes.append(current_prime)
            counter = current_prime
            while counter < max_prime:
                counter += current_prime
                primes_map[counter] = False

        current_prime += 1

    return primes


primes = generate_primes()

while True:
    x = int(input())

    if x == 0:
        break

    if x == 1:
        print(1)
        continue

    l = []

    for i in range(x):
        l.append(i + 1)

    p = primes[:x]
    pi = 0
    cp = 0
    while len(l) > 1:
        ps = p[pi]
        ps += cp
        ps -= 1

        if ps >= len(l):
            ps = ps % len(l)

        l.pop(ps)
        pi += 1
        cp = ps

    print(l[0])
