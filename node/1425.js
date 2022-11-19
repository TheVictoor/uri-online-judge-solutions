var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

for(line of lines) {
    let [stones, gift] = line.split(" ")
    
    if (stones == "0" && gift == "0") {
        return
    } 

    if (gift > 34) {
        console.log("Let me try")
    } else {
        stones = parseInt(stones)
        gift = parseInt(gift)
    
        let queue = []
        let win = false
    
        queue.push([2, 1])
    
        while (queue.length) {
            let [currentJump, currentStone] = queue.shift()
    
            if (currentStone == gift) {
                win = true
            }
    
            let nextJumpSize = currentJump * 2 - 1
            currentJump += 1
    
            let nextJumpAhead = currentStone + nextJumpSize
            let nextJumpBack = currentStone - nextJumpSize
    
            if (nextJumpAhead <= stones) {
                queue.push([currentJump, nextJumpAhead])
            }
    
            if (nextJumpBack > 0) {
                queue.push([currentJump, nextJumpBack])
            }
        }
    
        console.log(win ? "Let me try!" : "Don't make fun of me!")
    }
}
