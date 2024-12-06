def board_to_fen(board):
    fen = []
    
    for row in board:
        row_fen = ""
        empty_count = 0
        
        for square in row:
            if square == ".":
                empty_count += 1
            else:
                if empty_count > 0:
                    row_fen += str(empty_count)
                    empty_count = 0
                row_fen += square
        
        if empty_count > 0:
            row_fen += str(empty_count)
        
        fen.append(row_fen)
    
    return "/".join(fen)

board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

fen = board_to_fen(board)
print(fen)
