# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        while p != None:
            q = p
            p = p.next
        q.next = l2
        m = l1
        while m != None:
            while m.next != None:
                if m.val > m.next.val:
                    m.val, m.next.val = m.next.val, m.val
                m = m.next

        return l1