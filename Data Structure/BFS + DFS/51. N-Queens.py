def solveNQueens(n):
    results = []
    
    def draw(cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
    
    def isValid(cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if abs(r-row) == abs(c-col):
                return False
        return True
        
    def search(n,cols):
        row = len(cols)
        if row == n:
            results.append(draw(cols))
            return
        for cur_col in range(n):
            if not isValid(cols, row, cur_col):
                continue
            cols.append(cur_col)
            search(n,cols)
            cols.pop()
    search(n, [])
    return results

print(solveNQueens(4))