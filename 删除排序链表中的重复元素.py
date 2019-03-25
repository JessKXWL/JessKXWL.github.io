# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        q = head.next
        while q!=None:
            if p.val == q.val:
                p.next = p.next.next
                p = p.next
                q = p.next
            else:
                p = p.next
                q = p.next
        return head
