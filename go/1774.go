package main

import (
	"fmt"
)

type Node struct {
	weight int
	value  int
}

func main() {
	var r, c int

	fmt.Scanf("%d %d", &r, &c)

	dag := make(map[int][]Node)

	for i := 0; i < c; i++ {
		var a, b, p int
		fmt.Scanf("%d %d %d", &a, &b, &p)
		dag[a] = append(dag[a], Node{weight: p, value: b})
		dag[b] = append(dag[b], Node{weight: p, value: a})
	}

	visited_count := 1
	visited := make(map[int]bool)
	visited[1] = true

	nexts := []Node{}
	nexts = append(nexts, dag[1]...)

	total := 0
	for range dag {
		total += 1
	}

	shortest := 0

	for visited_count < total {
		var next Node
		var idx int
		for i, ni := range nexts {
			if ni.weight < next.weight || next.value == 0 {
				next = ni
				idx = i
			}
		}

		nexts = append(nexts[:idx], nexts[idx+1:]...)

		if visited[next.value] {
			continue
		}

		nexts = append(nexts, dag[next.value]...)

		shortest += next.weight

		visited[next.value] = true
		visited_count += 1
	}

	fmt.Printf("%d\n", shortest)

}
