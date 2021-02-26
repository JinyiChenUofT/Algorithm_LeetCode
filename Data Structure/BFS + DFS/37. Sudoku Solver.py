def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    def isValid(board, row, col, val):
        for i in range(9):
            if board[row][i] == val:
                return False
            if board[i][col] == val:
                return False
            if board[row//3*3 + i//3][col//3*3 + i%3] == val:
                return False
        return True
            
    def dfs(board, row, col):
        if col == 9:
            return dfs(board, row+1, 0)
        if row == 9:
            return True
        if board[row][col] != '.':
            return dfs(board, row, col+1)
            
        for val in range(1, 10):
            if not isValid(board, row, col, str(val)):
                continue
            board[row][col] = str(val)
            if dfs(board, row, col+1) is True:
                return True
            board[row][col] = '.'
        return False
    dfs(board,0,0)
    return board

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)