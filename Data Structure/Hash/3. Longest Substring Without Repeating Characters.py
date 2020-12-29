class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        res = 0 
        alphabet = [0 for i in range(256)]
        
        for c in s:
            end+=1
            alphabet[ord(c)-ord('a')] += 1
            if alphabet[ord(c)-ord('a')] > 1:
                res = max(res,end-start-1)
                while s[start] != c:
                    alphabet[ord(s[start])-ord('a')] -= 1
                    start += 1
                alphabet[ord(s[start])-ord('a')] -= 1
                start += 1
        res = max(res,end-start)
        return res

s = Solution()
s.lengthOfLongestSubstring("abcabcbb")