package main

import (
	"fmt"
)

type Visited struct {
	items []int
}

func (v Visited) add(x int) {
	add := true
	for _, i := range v.items {
		if i == x {
			add = false
		}
	}

	if add {
		v.items = append(v.items, x)
	}
}

func (v Visited) count() int {
	return len(v.items)
}

func bfs(parent int, visited Visited, current, start, total int, dag map[int][]int) int {
	visited.add(current)

	if visited.count() == total && current == start {
		return 0
	}

	c := 0
	if parent >= 0 {
		c = 2
	}

	nexts := dag[current]

	for _, n := range nexts {
		if n != parent {
			c += bfs(current, visited, n, start, total, dag)
		}
	}

	return c
}

func main() {
	var ntests int

	fmt.Scanf("%d", &ntests)

	for test := 0; test < ntests; test++ {
		var start int
		fmt.Scanf("%d", &start)

		var v, a int
		fmt.Scanf("%d %d", &v, &a)

		dag := make(map[int][]int)

		for i := 0; i < a; i++ {
			var fromA, toB int
			fmt.Scanf("%d %d", &fromA, &toB)

			addA := true

			for _, aa := range dag[fromA] {
				if aa == toB {
					addA = false
				}
			}

			if addA {
				dag[fromA] = append(dag[fromA], toB)
			}

			addB := true

			for _, bb := range dag[toB] {
				if bb == fromA {
					addB = false
				}
			}

			if addB {
				dag[toB] = append(dag[toB], fromA)
			}
		}

		keys := 0
		for range dag {
			keys += 1
		}

		// fmt.Printf("%v", dag)

		c := bfs(-1, Visited{}, start, start, keys, dag)

		fmt.Printf("%d\n", c)
	}
}
