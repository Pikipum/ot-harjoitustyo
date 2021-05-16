import piece

def can_move(board_grid, selected_pos_x, selected_pos_y, destination_pos_x, destination_pos_y):
    if selected_pos_x != None:
        board = board_grid
        name = board_grid[selected_pos_x-1][selected_pos_y-1].name
        destination = board_grid[destination_pos_x-1][destination_pos_y-1]

        if name == "WP": #Check which kind of piece it is
            if destination.name == "None":
                if selected_pos_x-destination_pos_x == 1 and selected_pos_y == destination_pos_y:
                    return True #Return True if the rules permit the move
                if selected_pos_x == 7 and selected_pos_x-destination_pos_x == 2 and selected_pos_y == destination_pos_y:
                    return True
            elif abs(selected_pos_y-destination_pos_y) == 1 and destination.name != "None":
                if selected_pos_x-destination_pos_x == 1:
                    return True
            else:
                return False
        elif name == "WKi":
            if abs(selected_pos_x - destination_pos_x) <= 1 and abs(selected_pos_y - destination_pos_y) <= 1:
                return True
            else:
                return False
        elif name == "WB":
            if abs(selected_pos_x - destination_pos_x) == abs(selected_pos_y - destination_pos_y):
                return True
            else:
                return False
        elif name == "WKn":
            return True
        elif name == "WR":
            if selected_pos_x == destination_pos_x or selected_pos_y == destination_pos_y:
                return True
        elif name == "WQ":                     
            if selected_pos_x == destination_pos_x or selected_pos_y == destination_pos_y:
                return True       
            if abs(selected_pos_x - destination_pos_x) == abs(selected_pos_y - destination_pos_y):
                return True
            else:
                return False
        elif name == "BB":
            if abs(selected_pos_x - destination_pos_x) == abs(selected_pos_y - destination_pos_y):
                return True
            else:
                return False
        elif name == "BP":
            if destination.name == "None":
                if selected_pos_x-destination_pos_x == -1 and selected_pos_y == destination_pos_y:
                    return True #Return True if the rules permit the move
                if selected_pos_x == 2 and selected_pos_x-destination_pos_x == -2 and selected_pos_y == destination_pos_y:
                    return True
            elif abs(selected_pos_y-destination_pos_y) == 1 and destination.name != "None":
                if selected_pos_x-destination_pos_x == -1:
                    return True
            else:
                return False
        elif name == "BR":        
            if selected_pos_x == destination_pos_x or selected_pos_y == destination_pos_y:
                return True
            else:
                return False
        elif name == "BQ":               
            if selected_pos_x == destination_pos_x or selected_pos_y == destination_pos_y:
                return True       
            if abs(selected_pos_x - destination_pos_x) == abs(selected_pos_y - destination_pos_y):
                return True
            else:
                return False
        elif name == "BKi":
            if abs(selected_pos_x - destination_pos_x) <= 1 and abs(selected_pos_y - destination_pos_y) <= 1:
                return True
            else:
                return False
        elif name == "BKn":
            return True
        else:
            return False