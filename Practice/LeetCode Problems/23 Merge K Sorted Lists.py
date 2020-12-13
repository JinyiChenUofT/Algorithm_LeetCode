import heapq

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

ListNode.__lt__ = lambda x,y : x.val< y.val
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
                heapq.heappush(heap,node.next)
        return dummy.next
        
head = ListNode(2)
head.next = ListNode(5)
head.next.next = ListNode(9)
head.next.next.next = ListNode(10)

head1 = ListNode(1)
head1.next = ListNode(6)
head1.next.next = ListNode(7)
head1.next.next.next = ListNode(10)

lists = []
lists.append(head)
lists.append(head1)

s = Solution()
s.mergeKLists(lists)