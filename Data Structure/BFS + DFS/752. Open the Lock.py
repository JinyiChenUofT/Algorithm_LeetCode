import collections

class Solution:
    def openLock(self, deadends, target):
        def nextSteps(node):
            nextSteps = []
            for i in range(len(node)):
                left, mid, right = node[:i], node[i], node[i+1:]
                mid = int(mid)
                for mid in [(mid + 1)% 10, (mid - 1) % 10]:
                    nextSteps.append(left+str(mid)+right)
            return nextSteps
        
        queue = collections.deque([('0000',0)])
        seen = {'0000'}
        
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth

            if node in deadends:
                continue
            for nextNode in nextSteps(node):
                if nextNode not in seen:
                    seen.add(nextNode)
                    queue.append([nextNode,depth+1])

        return -1

s = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = '0202'
print(s.openLock(deadends,target))