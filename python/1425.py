
while 1:
    stones, gift = input().split(" ")
    stones, gift = int(stones), int(gift)

    if stones == 0 and gift == 0:
        break

    queue = []

    queue.append([1, 1])

    win = 0

    while queue:
        current_jump, curr_stone = queue.pop(0)

        if curr_stone < 1 or curr_stone > stones:
            continue

        if curr_stone == gift:
            win = 1
            break

        current_jump += 1
        next_jump_size = current_jump * 2 - 1
        
        next_stone_jump_ahead = curr_stone + next_jump_size
        next_stone_jump_back = curr_stone - next_jump_size

        queue.append([current_jump, next_stone_jump_ahead])
        queue.append([current_jump, next_stone_jump_back])

        
    print("Let me try!" if win else "Don't make fun of me!")

