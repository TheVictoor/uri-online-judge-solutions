import queue

n_cases = int(input())


def figure_out_spot_for_item(item, board):
    for row_index, row in enumerate(board):
        for col_index, col_item in enumerate(row):
            if col_item == item:
                return (
                    row_index,
                    col_index,
                    0,
                    item,
                    str(row_index) + str(col_index),
                    [],
                )


def get_next_spot_for_move(move, spot, board, next_step):
    next_spot = None
    board_size = len(board)

    if move == "R" and spot[1] + 1 < board_size:
        next_row = spot[0]
        next_col = spot[1] + 1
        next_spot = (
            next_row,
            next_col,
            next_step,
            board[next_row][next_col],
            str(next_row) + str(next_col),
        )
    elif move == "D" and spot[0] + 1 < board_size:
        next_row = spot[0] + 1
        next_col = spot[1]
        next_spot = (
            next_row,
            next_col,
            next_step,
            board[next_row][next_col],
            str(next_row) + str(next_col),
        )
    elif move == "L" and spot[1] > 0:
        next_row = spot[0]
        next_col = spot[1] - 1
        next_spot = (
            next_row,
            next_col,
            next_step,
            board[next_row][next_col],
            str(next_row) + str(next_col),
        )
    elif move == "U" and spot[0] > 0:
        next_row = spot[0] - 1
        next_col = spot[1]
        next_spot = (
            next_row,
            next_col,
            next_step,
            board[next_row][next_col],
            str(next_row) + str(next_col),
        )
    else:
        return spot

    if next_spot[3] != "#":
        return next_spot

    return spot


def get_neighbors_for_spot(spot_a, spot_b, spot_c, graph):
    neighbors = []
    next_moves_a = graph[spot_a[4]]
    next_moves_b = graph[spot_b[4]]
    next_moves_c = graph[spot_c[4]]

    merged_moves = zip(next_moves_a, next_moves_b, next_moves_c)
    next_step = spot_a[2] + 1

    for moves in merged_moves:
        a, b, c = moves

        a, b, c = fix_moves(spot_a, spot_b, spot_c, a, b, c)

        neighbors.append(
            [
                (a[0], a[1], next_step, a[3], a[4]),
                (b[0], b[1], next_step, b[3], b[4]),
                (c[0], c[1], next_step, c[3], c[4]),
            ]
        )

    return neighbors


def fix_moves(spot_a, spot_b, spot_c, a, b, c):
    if c[4] == b[4] or c[4] == a[4]:
        c = spot_c

    if b[4] == c[4] or b[4] == a[4]:
        b = spot_b
        if c[4] == b[4] or c[4] == a[4]:
            c = spot_c

    if a[4] == c[4] or a[4] == b[4]:
        a = spot_a
        if b[4] == c[4] or b[4] == a[4]:
            b = spot_b
        if c[4] == b[4] or c[4] == a[4]:
            c = spot_c
    return a, b, c


def get_unique_identifier(spots):
    return "".join([spots[0][4], spots[1][4], spots[2][4]])


def map_board_as_a_graph(board):
    graph = {}

    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            spot = (
                row_index,
                col_index,
                0,
                board[row_index][col_index],
                str(row_index) + str(col_index),
            )
            moves = [
                get_next_spot_for_move("R", spot, board, 0),
                get_next_spot_for_move("D", spot, board, 0),
                get_next_spot_for_move("L", spot, board, 0),
                get_next_spot_for_move("U", spot, board, 0),
            ]
            graph[spot[4]] = moves

    return graph


def BFS(spot_a, spot_b, spot_c, target, graph):
    neighbors = get_neighbors_for_spot(spot_a, spot_b, spot_c, graph)
    q = queue.SimpleQueue()
    to_visit = {}
    to_visit[get_unique_identifier([spot_a, spot_b, spot_c])] = 1

    for neighbor in neighbors:
        q.put(neighbor)
        to_visit[get_unique_identifier(neighbor)] = 1

    while not q.empty():
        current_neighbor = q.get()
        spot_a, spot_b, spot_c = current_neighbor

        if spot_a[3] == target and spot_b[3] == target and spot_c[3] == target:
            return spot_a

        next_moves_a = graph[spot_a[4]]
        next_moves_b = graph[spot_b[4]]
        next_moves_c = graph[spot_c[4]]

        merged_moves = zip(next_moves_a, next_moves_b, next_moves_c)
        next_step = spot_a[2] + 1

        for moves in merged_moves:
            a, b, c = moves

            a, b, c = fix_moves(spot_a, spot_b, spot_c, a, b, c)

            neighbor = [
                (a[0], a[1], next_step, a[3], a[4]),
                (b[0], b[1], next_step, b[3], b[4]),
                (c[0], c[1], next_step, c[3], c[4]),
            ]

            key = "".join([neighbor[0][4], neighbor[1][4], neighbor[2][4]])
            if not to_visit.get(key):
                to_visit[key] = 1
                q.put(neighbor)


for case in range(n_cases):
    board_size = int(input())
    board = []

    for board_line in range(board_size):
        board.append(list(input()))

    a = figure_out_spot_for_item("A", board)
    b = figure_out_spot_for_item("B", board)
    c = figure_out_spot_for_item("C", board)

    graph = map_board_as_a_graph(board)
    final_spot = BFS(a, b, c, "X", graph)
    message = final_spot[2] if final_spot else "trapped"
    print(f"Case {case+1}: {message}")
