package '1020'

import (
	"fmt"
)

func main() {
	var days int

	fmt.Scanf("%d", &days)

	years := days / 365
	years_rest := days % 365
	months := years_rest / 30
	montts_rest := years_rest % 30

	fmt.Printf("%v ano(s)\n", years)
	fmt.Printf("%v mes(es)\n", months)
	fmt.Printf("%v dia(s)\n", montts_rest)
}
