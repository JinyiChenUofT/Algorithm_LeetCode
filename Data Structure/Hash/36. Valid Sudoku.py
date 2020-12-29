class Solution:
    def isValidSudoku(self, board):
        seen = []
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    seen.append((i,num))
                    seen.append((num,j))
                    seen.append((i//3,j//3,num))
        print(seen)
        return len(seen) == len(set(seen))

board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
s = Solution()
s.isValidSudoku(board)