class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if board == None or len(board)==0 or len(board[0])==0:
            return
        m, n = len(board), len(board[0])
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        def bfs(board, i, j):
            if board[i][j]!='O':
                return
            import queue
            qx = queue.Queue()
            qy = queue.Queue()
            qx.put(i)
            qy.put(j)
            board[i][j] = 'W'
            while not qx.empty():
                cx = qx.get()
                cy = qy.get()
                for d in range(4):
                    nx = cx + dx[d]
                    ny = cy + dy[d]
                    if nx>=0 and nx<m and ny>=0 and ny<n and board[nx][ny]=='O':
                        board[nx][ny]='W'
                        qx.put(nx)
                        qy.put(ny)

        
        for i in range(m):
            bfs(board, i, 0)
            bfs(board, i, n-1)
        for j in range(n):
            bfs(board, 0, j)
            bfs(board, m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'W':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
s = Solution()
board = [["O","O","O"],["O","O","O"],["O","O","O"]]
s.solve(board)