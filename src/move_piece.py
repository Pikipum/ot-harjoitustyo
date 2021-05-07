import piece

def can_move(piece, destination):

    name = piece.name
    if name == "WP": #Check which kind of piece it is
        return True #Return True if the rules permit the move
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