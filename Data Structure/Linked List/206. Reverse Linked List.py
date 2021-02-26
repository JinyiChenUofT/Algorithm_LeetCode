# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur.next:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

            print(cur, " ", prev)
        cur.next = prev
        return cur


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
s.reverseList(head)