import collections
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

a = {}
l = [0,1]
#a[l]= 'a' 
#print(a) #TypeError: unhashable type: 'list'

a[tuple(l)] = 'a'
print (a)