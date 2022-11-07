from collections import namedtuple
import queue

Spot = namedtuple("Spot", ["row", "col", "steps", "won"])

n_cases = int(input())


def figure_out_spot_for_item(item, board):
    for row_index, row in enumerate(board):
        for col_index, col_item in enumerate(row):
            if col_item == item:
                return Spot(row_index, col_index, 0, False)


def is_equal_spot(spot, spot_a, spot_b):
    return (spot.row == spot_a.row and spot.col == spot_a.col) or (spot.row == spot_b.row and spot.col == spot_b.col)


def check_move_is_valid(move, spot, board_size):
    if move == "R" and spot.col + 1 < board_size:
        return True
    elif move == "D" and spot.row + 1 < board_size:
        return True
    elif move == "L" and spot.col > 0:
        return True
    elif move == "U" and spot.row > 0:
        return True

    return False
    

def get_next_spot_for_move(move, spot: Spot, board, next_step):
    next_spot = None
    board_size = len(board)
    if check_move_is_valid(move, spot, board_size):
        if move == "R" :
            next_spot = Spot(spot.row, spot.col+1, next_step, False)
        elif move == "D":
            next_spot = Spot(spot.row+1, spot.col, next_step, False)
        elif move == "L":
            next_spot = Spot(spot.row, spot.col-1, next_step, False)
        elif move == "U":
            next_spot = Spot(spot.row-1, spot.col, next_step, False)

    if next_spot and get_value(next_spot, board) != "#":
        return next_spot

    return spot


def get_neighbors_for_spot(spot: Spot, spot_b, spot_c, board):
    neighbors = []

    new_spot = get_spot_for_move('R', spot, spot_b, spot_c, board, spot.steps + 1)    
    neighbors.append(new_spot)

    new_spot = get_spot_for_move('D', spot, spot_b, spot_c, board, spot.steps + 1)    
    neighbors.append(new_spot)

    new_spot = get_spot_for_move('L', spot, spot_b, spot_c, board, spot.steps + 1)    
    neighbors.append(new_spot)

    new_spot = get_spot_for_move('U', spot, spot_b, spot_c, board, spot.steps + 1)    
    neighbors.append(new_spot)
        
    return neighbors


def get_spot_for_move(move, spot: Spot, spot_b, spot_c, board, next_step):
    spot = Spot(spot.row, spot.col, next_step, False)
    next_b = get_next_spot_for_move(move, spot_b, board, next_step)
    next_c = get_next_spot_for_move(move, spot_c, board, next_step)
    new_spot = get_next_spot_for_move(move, spot, board, next_step)

    if is_equal_spot(next_b, next_c, new_spot):
        next_b = spot_b

    if is_equal_spot(next_c, next_b, new_spot):
        next_c = spot_c

    if is_equal_spot(new_spot, next_b, next_c):
        new_spot = spot

    return new_spot


def get_neighbors(spots: tuple[Spot, Spot, Spot], board):
    neighbor_a, neighbor_b, neighbor_c = spots

    return list(zip(
        get_neighbors_for_spot(neighbor_a, neighbor_b, neighbor_c, board),
        get_neighbors_for_spot(neighbor_b, neighbor_c, neighbor_a, board),
        get_neighbors_for_spot(neighbor_c, neighbor_a, neighbor_b, board)
    ))


def get_value(spot: Spot, board: list[list[str]]):
    return board[spot.row][spot.col]


def get_as_string(spot: Spot):
    return f"{spot.row}{spot.col}"


def check_if_is_visited(visited: set[str], spots: tuple[Spot, Spot, Spot]):
    neighbor_a, neighbor_b, neighbor_c = spots
    key = get_as_string(neighbor_a) + get_as_string(neighbor_b) + get_as_string(neighbor_c)
    return key in visited


def BFS(spot_a: Spot, spot_b: Spot, spot_c: Spot, target: str, board: list[list[str]]):
    won = None

    neighbors = get_neighbors((spot_a, spot_b, spot_c), board)

    q = queue.SimpleQueue()

    for neighbor in neighbors: 
        q.put(neighbor)

    visited =  set()
    while not q.empty():
        current_neighbor: tuple[Spot, Spot, Spot] = q.get()
        spot_a, spot_b, spot_c = current_neighbor

        if check_if_is_visited(visited, current_neighbor):
            continue

        if get_value(spot_a, board) == target and get_value(spot_b, board) == target and get_value(spot_c, board) == target:
            won  = spot_a 
            break

        visited.add(
            get_as_string(spot_a) + get_as_string(spot_b) + get_as_string(spot_c)
        )

        spot_neighbors = get_neighbors(current_neighbor, board)

        for neighbor in spot_neighbors: 
            spot_a, spot_b, spot_c = neighbor
            if get_as_string(spot_a) + get_as_string(spot_b) + get_as_string(spot_c) not in visited:
                q.put(neighbor)
        
    return won


for case in range(n_cases):
    board_size = int(input())
    board = []
    for board_line in range(board_size):
        board.append(list(input()))

    a = figure_out_spot_for_item("A", board)
    b = figure_out_spot_for_item("B", board)
    c = figure_out_spot_for_item("C", board)
    moves_to_reach = BFS(a, b, c, "X", board)
    message = moves_to_reach.steps if moves_to_reach else "trapped"
    # moves= "" if not moves_to_reach else "".join(moves_to_reach.moves)
    print(f"Case {case+1}: {message}")
