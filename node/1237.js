var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

/**
 * Escreva a sua solução aqui
 * Code your solution here
 * Escriba su solución aquí
 */

while (lines.length) {
    let word1 = lines.shift()
    let word2 = lines.shift()

    if (!word1 || !word2) {
        break
    }

    word1 = word1.split("")
    word2 = word2.split("")

    let grid = []

    word2.forEach((letter2, rowIndex) => {
        grid.push([])

        word1.forEach((letter1, colIndex) => {
            let value = 0
            if (letter1 != letter2) {
                grid[rowIndex].push(value)
                return
            }

            value = 1

            if (rowIndex === 0 || colIndex === 0) {
                grid[rowIndex].push(value)
                return
            }

            value += grid[rowIndex - 1][colIndex - 1]
            grid[rowIndex].push(value)
        })
    })

    let maxValue = 0
    grid.forEach((row) => {
        row.forEach((col) => {
            if (col > maxValue) {
                maxValue = col
            }
        })
    })

    console.log(maxValue)
    
}