package main

import (
	"fmt"
)

func main() {
	primes := getPrimes()

	for true {
		var c int

		fmt.Scanln(&c)

		if c == 0 {
			return
		}

		l := make([]int, c)

		for i := range l {
			l[i] = i + 1
		}

		pi := 0
		cp := 0

		for len(l) > 1 {
			pos := primes[pi]
			pos += cp
			pos -= 1

			if pos >= len(l) {
				pos = pos % len(l)
			}

			l = append(l[:pos], l[pos+1:]...)

			pi += 1
			cp = pos
		}

		fmt.Printf("%v\n", l[0])
	}
}

func getPrimes() []int {
	primeMap := make(map[int]bool)

	maxPrime := 40000

	primes := make([]int, 0)
	primes = append(primes, 2)
	currentPrime := 3

	for len(primes) < 3501 {
		if currentPrime%2 != 0 && !primeMap[currentPrime] {
			primes = append(primes, currentPrime)

			counter := currentPrime
			for counter <= maxPrime {
				counter += currentPrime
				primeMap[counter] = true
			}
		}

		currentPrime += 1
	}

	return primes
}
