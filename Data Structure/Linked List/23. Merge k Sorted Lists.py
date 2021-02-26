# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

ListNode.__lt__ = lambda x,y : (x.val < y.val)
class Solution:
    def mergeKLists(self, lists):
        
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap,head)
        
        dummy = ListNode(0)
        cur = dummy
        while heap:
            node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            
            if node.next:
                heapq.heappush(heap, node.next)
        return dummy.next

a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

c = ListNode(2)
c.next = ListNode(6)

l = []
l.append(a)
l.append(b)
l.append(c)

s = Solution()
s.mergeKLists(l)