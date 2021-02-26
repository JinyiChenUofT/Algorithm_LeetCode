class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        from collections import defaultdict
        if len(words) == 0:
            return []
        res = []
        prefix = defaultdict(list)
        squares = []
        #预处理得到prefix
        def initprefix(words):
            for word in words:
                prefix[""].append(word)
                pre = ""
                for i in range(len(word)):
                    pre += word[i]
                    prefix[pre].append(word)
        def checkprefix(index,Next):
            print("index,Next: ",index,Next)
            for i in range(index+1,wordlen):
                pre = ""
                for j in range(index):
                    pre += squares[j][i]
                pre += Next[i]
                if pre not in prefix:
                    return False
            return True
        def dfs(index):
            if index == wordlen:
                res.append(squares[:])
                return
            pre = ""
            print("squares: ",squares)
            for i in range(index):
                pre += squares[i][index]
            matchedword = prefix[pre][:]
            print("matchedword: ",matchedword)
            m = len(matchedword)
            for i in range(m):
                #找到pre前缀
                if checkprefix(index,matchedword[i]) == False:
                    continue
                squares.append(matchedword[i])
                dfs(index + 1)
                squares.pop()
                
        initprefix(words)
        wordlen = len(words[0])
        dfs(0)
        return res

s = Solution()
res = s.wordSquares(["area","lead","wall","lady","ball"])
print(res)