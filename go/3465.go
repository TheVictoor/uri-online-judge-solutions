package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b, c float64

	fmt.Scanf("%f %f %f", &a, &b, &c)

	p := (a + b + c) / 2

	area := math.Sqrt(p * (p - a) * (p - b) * (p - c))

	fmt.Printf("%.3f m2\n", area)
}
