import piece

def can_move(board_grid, selected_pos_x, selected_pos_y, destination_pos_x, destination_pos_y):

    board = board_grid
    name = board_grid[selected_pos_x-1][selected_pos_y-1].name
    destination = board_grid[destination_pos_x][destination_pos_y]

    if name == "WP": #Check which kind of piece it is
        if destination.name == "None":
            if selected_pos_x-destination_pos_x == 1 and selected_pos_y == destination_pos_y:
                return True #Return True if the rules permit the move
            if selected_pos_x == 7 and selected_pos_x-destination_pos_x == 2:
                return True
        elif abs(selected_pos_y-destination_pos_y) == 1 and destination.name != "None":
            if selected_pos_x-destination_pos_x == 1:
                return True
        else:
            return False
    elif name == "WK":
        return True
    elif name == "WB":
        return True
    elif name == "WK":
        return True
    elif name == "WR":
        return True
    elif name == "WQ":
        return True
    elif name == "BB":
        return True
    elif name == "BP":
        return True
    elif name == "BR":
        return True
    elif name == "BQ":
        return True
    elif name == "BK":
        return True
    else:
        return False