
while True: 
    try:
        word1 = input()
        word2 = input()

        grid = []

        for row_index, letter2 in enumerate(word2): 
            grid.append([])
            for col_index, letter1 in enumerate(word1):
                value = 0
                if letter1 != letter2:
                    grid[row_index].append(value)
                    continue

                value = 1

                if row_index == 0 or col_index == 0:
                    grid[row_index].append(value)
                    continue

                value += grid[row_index - 1][col_index - 1]
                grid[row_index].append(value)
            
        max_value = 0
        for row in grid:
            for col_value in row:
                if col_value > max_value:
                    max_value = col_value
        
        print(max_value)

    except:
        break
