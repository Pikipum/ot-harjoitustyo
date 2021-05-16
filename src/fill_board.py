import piece

def fill(grid, length):

    #Fill the board with pieces, empty spots are pieces with None name
    
    grid[0] = [piece.Piece("BR", 60, 60), piece.Piece("BKn", 60, 60), 
    piece.Piece("BB", 60, 60), piece.Piece("BQ", 60, 60), 
    piece.Piece("BKi", 60, 60), piece.Piece("BB", 60, 60), 
    piece.Piece("BKn", 60, 60), piece.Piece("BR", 60, 60)]
    grid[1] = [piece.Piece("BP", 60, 60), 
    piece.Piece("BP", 60, 60), piece.Piece("BP", 60, 60), 
    piece.Piece("BP", 60, 60), piece.Piece("BP", 60, 60), 
    piece.Piece("BP", 60, 60), piece.Piece("BP", 60, 60), 
    piece.Piece("BP", 60, 60)]
    grid[2] = [piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60)]
    grid[3] = [piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60)]
    grid[4] = [piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60)]
    grid[5] = [piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60), 
    piece.Piece("None", 60, 60), piece.Piece("None", 60, 60)]
    grid[6] = [piece.Piece("WP", 60, 60), 
    piece.Piece("WP", 60, 60), piece.Piece("WP", 60, 60), 
    piece.Piece("WP", 60, 60), piece.Piece("WP", 60, 60), 
    piece.Piece("WP", 60, 60), piece.Piece("WP", 60, 60), 
    piece.Piece("WP", 60, 60)]
    grid[7] = [piece.Piece("WR", 60, 60), piece.Piece("WKn", 60, 60), 
    piece.Piece("WB", 60, 60), piece.Piece("WQ", 60, 60), 
    piece.Piece("WKi", 60, 60), piece.Piece("WB", 60, 60), 
    piece.Piece("WKn", 60, 60), piece.Piece("WR", 60, 60)]

    return grid