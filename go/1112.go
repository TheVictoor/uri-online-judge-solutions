package main

import (
	"fmt"
)

func updateBIT(bit [][]int, x, yy, val, X, Y int) {
	for x <= X {
		y := yy
		for y <= Y {
			bit[x][y] += val
			y += y & -y
		}
		x += x & -x
	}
}

func getSum(bit [][]int, x, yy int) int {
	sum := 0
	for x > 0 {
		y := yy
		for y > 0 {
			sum += bit[x][y]
			y -= y & -y
		}
		x -= x & -x
	}
	return sum
}

func answerQueries(x1, y1, x2, y2 int, bit [][]int) int {
	v1 := getSum(bit, x2, y2)
	v2 := getSum(bit, x2, y1-1)
	v3 := getSum(bit, x1-1, y2)
	v4 := getSum(bit, x1-1, y1-1)

	return v1 - v2 - v3 + v4
}

func main() {
	for {
		var x, y, p, q int
		fmt.Scanf("%d %d %d", &x, &y, &p)

		if x == 0 && y == 0 && p == 0 {
			break
		}

		fmt.Scanf("%d", &q)

		bit := make([][]int, x+1)
		for i := range bit {
			bit[i] = make([]int, y+1)
			for idx := range bit[i] {
				bit[i][idx] = 0
			}
		}

		for i := 0; i < q; i++ {
			a := ""
			fmt.Scanf("%s", &a)

			if a == "A" {
				var an, ax, ay int
				fmt.Scanf("%d %d %d", &an, &ax, &ay)

				updateBIT(bit, ax+1, ay+1, an, x, y)
			} else {
				var fx, fy, ux, uy int

				fmt.Scanf("%d %d %d %d", &fx, &fy, &ux, &uy)

				x1, x2 := ux, fx
				if x2 < x1 {
					x1, x2 = x2, x1
				}

				y1, y2 := uy, fy
				if y2 < y1 {
					y1, y2 = y2, y1
				}

				ans := answerQueries(x1+1, y1+1, x2+1, y2+1, bit)

				fmt.Println(ans * p)
			}
		}
		fmt.Println()
	}
}

