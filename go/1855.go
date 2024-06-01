package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var c, r int
	fmt.Scan(&c, &r)

	var grid [][]rune
	for i := 0; i < r; i++ {
		line, _ := reader.ReadString('\n')
		grid = append(grid, []rune(strings.TrimSpace(line)))
	}

	visited := make(map[string]bool)
	direction := ""
	current := [2]int{0, 0}

	getCurrent := func(curr [2]int) rune {
		return grid[curr[0]][curr[1]]
	}

	for !visited[fmt.Sprintf("%v", current)] && getCurrent(current) != '*' {
		visited[fmt.Sprintf("%v", current)] = true
		currentCell := getCurrent(current)
		if currentCell == '>' || currentCell == '<' || currentCell == 'v' || currentCell == '^' {
			direction = string(currentCell)
		}

		switch direction {
		case ">":
			if current[1]+1 >= c {
				break
			}
			current[1]++
		case "<":
			if current[1]-1 < 0 {
				break
			}
			current[1]--
		case "v":
			if current[0]+1 >= r {
				break
			}
			current[0]++
		case "^":
			if current[0]-1 < 0 {
				break
			}
			current[0]--
		}
	}

	if getCurrent(current) != '*' {
		fmt.Println("!")
	} else {
		fmt.Println("*")
	}
}
