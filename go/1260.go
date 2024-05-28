package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var ntests int
	fmt.Scanf("%d", &ntests)

	var input string
	fmt.Scanln(&input)

	trees := make(map[string]float64)
	var total float64 = 0.0

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		input = scanner.Text()

		if input == "" {
			var keys []string
			for k := range trees {
				keys = append(keys, k)
			}
			sort.Strings(keys)
			for _, k := range keys {
				var r float64 = trees[k] * 100 / total
				fmt.Printf("%v %.4f\n", k, r)
			}
			fmt.Printf("\n")

			total = 0
			trees = make(map[string]float64)
			continue
		}

		trees[input] += 1.0
		total += 1.0
	}

	var keys []string
	for k := range trees {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	for _, k := range keys {
		fmt.Printf("%v %.4f\n", k, trees[k]*100/total)
	}
}
