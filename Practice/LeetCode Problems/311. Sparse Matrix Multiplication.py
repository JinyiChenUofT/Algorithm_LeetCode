class Solution:
    def multiply(self, A, B):
        m = len(A)
        n = len(B[0])
        l = len(A[0])
        
        res = [[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                for k in range(l):
                    res[i][j] += A[i][k]*B[k][j]
        return res
'''
class Solution:
    def multiply(self, A, B):
        m = len(A)
        n = len(B[0])
        l = len(A[0])
        p = len(B)
        
        res = [[0]*n for i in range(m)]
        
        col = []
        for i in range(p):
            row = []
            for j in range(n):
                if B[i][j]!=0:
                    row.append(j)
            col.append(row)
                
        for i in range(m):
            for k in range(l):
                if A[i][k] == 0:
                    continue
                for j in col[k]:
                    res[i][j] += A[i][k]*B[k][j]
        return res
'''

s = Solution()
A = [[1,-5]]
B = [[12],[-1]]
s.multiply(A,B)