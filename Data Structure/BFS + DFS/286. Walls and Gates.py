class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(rooms,x,y,index):
            if rooms[n][y]== 2147483647:
                rooms[x][y] = index+1
            else:
                cur_index = rooms[x][y]
                if cur_index>index+1:
                    rooms[x][y] = index+1
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx>=0 and nx< m and ny>=0 and ny<n and rooms[nx][ny]!='-1'and rooms[nx][ny]!='0':
                    bfs(rooms,nx,ny,index+1)
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j]=='0':
                    bfs(rooms,i,j,0)
        

s = Solution()
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
s.wallsAndGates(rooms)