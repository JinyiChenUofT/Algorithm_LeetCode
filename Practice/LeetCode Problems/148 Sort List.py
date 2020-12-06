# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def findMid_wrong(self, head):
        if not head or not head.next:
            return head
        slow, fast = head,head

        # I was hoping when fast is None, it will jump out of the loop, but it finishes the operation of slow = slow.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
    
    def findMid(self, head):
        if not head or not head.next:
            return head
        slow, fast = head,head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

    # O(nlogn)    
    def sortList(self, head: ListNode) -> ListNode: 
        if not head or not head.next:
            return head

        mid = self.findMid(head)  # O(n)
        left = head
        right = mid.next
        mid.next = None

        sortList_left = self.sortList(left) # O(logn)
        sortList_right = self.sortList(right) # O(logn)

        return self.merge(sortList_left, sortList_right)

    def ListVals(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
# 4->2->1->3
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
s = Solution()
res = s.sortList(head)
print(res.val)