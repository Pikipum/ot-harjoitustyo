import piece

def fill(grid, length):
    
    #grid[0] = ["BT", "BH", "BB", "BQ", "BK", "BB", "BH", "BT"]
    #grid[1] = ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"]
    grid[0] = [piece.Piece("BR", 60, 60), piece.Piece("BK", 60, 60), 
    piece.Piece("BB", 60, 60), piece.Piece("BQ", 60, 60), 
    piece.Piece("BK", 60, 60), piece.Piece("BB", 60, 60), 
    piece.Piece("BK", 60, 60), piece.Piece("BR", 60, 60)]
    grid[1] = [piece.Piece("BP", 60, 60), 
    piece.Piece("BP", 60, 60), piece.Piece("BP", 60, 60), 
    piece.Piece("BP", 60, 60), piece.Piece("BP", 60, 60), 
    piece.Piece("BP", 60, 60), piece.Piece("BP", 60, 60), 
    piece.Piece("BP", 60, 60)]
    grid[6] = [piece.Piece("WP", 60, 60), 
    piece.Piece("WP", 60, 60), piece.Piece("WP", 60, 60), 
    piece.Piece("WP", 60, 60), piece.Piece("WP", 60, 60), 
    piece.Piece("WP", 60, 60), piece.Piece("WP", 60, 60), 
    piece.Piece("WP", 60, 60)]
    grid[7] = [piece.Piece("WR", 60, 60), piece.Piece("WK", 60, 60), 
    piece.Piece("WB", 60, 60), piece.Piece("WQ", 60, 60), 
    piece.Piece("WK", 60, 60), piece.Piece("WB", 60, 60), 
    piece.Piece("WK", 60, 60), piece.Piece("WR", 60, 60)]
    #grid[6] = ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"]
    #grid[7] = ["WT", "WH", "WB", "WQ", "WK", "WB", "WH", "WT"]

    return grid