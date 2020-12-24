class Solution:
    def getAbbreviation(self, s, index):
        if index >= len(s)-2:
            return s
        lens = len(s)
        return s[0:index]+str(lens-index-1)+s[-1]
        
    def wordsAbbreviation(self, dict):
        dic = {}
        res = []
        index = 1
        lend = len(dict)
        conflicts = [True]*lend
        for s in dict:
            abb_s = self.getAbbreviation(s,index)
            dic[abb_s] = dic.get(abb_s,0) + 1
            res.append(abb_s)
        
        
        while conflicts != [False]*lend:
            index+=1
            for i in range(lend):
                if dic[res[i]] == 1:
                    conflicts[i] = False
                else:
                    abb_s = self.getAbbreviation(dict[i],index)
                    dic[abb_s] = dic.get(abb_s,0) + 1
                    res[i] = abb_s
        return res
            
s = Solution()
dict = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
s.wordsAbbreviation(dict)