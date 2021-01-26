import collections
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:      
        def nextPuzzles(board):
            directions = ((0,1),(1,0),(0,-1),(-1,0))
            res = []
            zero_index = board.find('0')
            x, y = zero_index//3, zero_index%3
            for d in range(4):
                new_x,new_y = x+directions[d][0], y+directions[d][1]
                if 0<=new_x<2 and 0<=new_y<3:
                    new_board = list(board)
                    new_board[x*3+y] = new_board[new_x*3+new_y]
                    new_board[new_x*3+new_y] = '0'
                    res.append("".join(new_board))
            return res
        
        def matrixToString(matrix):
            onelist = []
            for i in range(2):
                for j in range(3):
                    onelist.append(str(matrix[i][j]))
            return "".join(onelist)
        
        source = matrixToString(board)
        target = matrixToString([[1,2,3],[4,5,0]])
        queue = collections.deque([(source,0)])
        seen = {source}
        while queue:
            cur_board, step = queue.popleft()
            
            if cur_board == target:
                return step
            
            for next_board in nextPuzzles(cur_board):
                if next_board in seen:
                    continue
                seen.add(next_board)
                queue.append([next_board,step+1])

        return -1

s = Solution()
board = [[4,1,2],[5,0,3]]
s.slidingPuzzle(board)