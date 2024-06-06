package main

import (
	"fmt"
)

func nextMoves(matrix [5][5]int, visited map[[2]int]bool, current [2]int) [][2]int {
	var nexts [][2]int

	right := [2]int{current[0], current[1] + 1}
	down := [2]int{current[0] + 1, current[1]}
	left := [2]int{current[0] - 1, current[1]}
	up := [2]int{current[0], current[1] - 1}

	if right[1] < 5 && matrix[right[0]][right[1]] == 0 && visited[right] == false {
		nexts = append(nexts, right)
	}

	if down[0] < 5 && matrix[down[0]][down[1]] == 0 && visited[down] == false {
		nexts = append(nexts, down)
	}

	if up[1] >= 0 && matrix[up[0]][up[1]] == 0 && visited[up] == false {
		nexts = append(nexts, up)
	}

	if left[0] >= 0 && matrix[left[0]][left[1]] == 0 && visited[left] == false {
		nexts = append(nexts, left)
	}

	return nexts
}

func dfs(matrix [5][5]int, current [2]int, visited map[[2]int]bool) bool {
	if current[0] == 4 && current[1] == 4 {
		return true
	}

	visited[current] = true

	nexts := nextMoves(matrix, visited, current)

	for _, n := range nexts {
		result := dfs(matrix, n, visited)
		if result {
			return result
		}
		visited[n] = false
	}

	return false
}

func main() {
	var cases int
	fmt.Scanf("%d", &cases)

	for c := 0; c < cases; c++ {
		var matrix [5][5]int

		for r := 0; r < 5; r++ {
			for j := 0; j < 5; j++ {
				i, _ := fmt.Scanf("%d", &matrix[r][j])
				if i != 1 {
					j--
				}
			}
		}

		result := false
		if matrix[0][0] == 0 {
			visited := make(map[[2]int]bool)
			result = dfs(matrix, [2]int{0, 0}, visited)
		}

		if result {
			fmt.Printf("COPS\n")
		} else {
			fmt.Printf("ROBBERS\n")
		}
	}
}
