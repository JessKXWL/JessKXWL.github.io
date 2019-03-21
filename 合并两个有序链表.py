# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        p = l1
        q = None
        while p != None:
            q = p
            p = p.next
        q.next = l2
        l1 = self.sortListNode(l1)
        return l1

    def sortListNode(self, l1: ListNode) -> ListNode:

        # write your code here
        if (l1 == None): return l1

        def findmid(head):
            count = 0
            save = head
            while (head != None):
                head = head.next
                count += 1
            i = 0
            while (True):

                i += 1
                if (i >= count / 2): break
                save = save.next
            return save

        def merge(left, right):
            pre = ListNode(None)
            save = pre
            while (left != None and right != None):
                if (left.val < right.val):
                    pre.next = left
                    pre = left
                    left = left.next
                else:
                    pre.next = right
                    pre = right
                    right = right.next
            if (left == None):
                while (right != None):
                    pre.next = right
                    pre = right
                    right = right.next

            if (right == None):
                while (left != None):
                    pre.next = left
                    pre = left
                    left = left.next

            return save.next

        def mergeSort(head):
            if (head.next == None): return head
            mid = findmid(head)
            midn = mid.next
            mid.next = None
            left = mergeSort(head)
            right = mergeSort(midn)

            result = merge(left, right)
            return result

        result = mergeSort(l1)
        return result

class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = tmp = ListNode(-1)
        while l1 and l2:
            if l1.val>l2.val:
                tmp.next = l2
                l2 = l2.next
            else:
                tmp.next = l1
                l1 = l1.next
            tmp = tmp.next
        tmp.next = l1 if l1 else l2
        return head.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    so = Solution1()
    l3 = so.mergeTwoLists(l1,l2)
    p = l3
    while p!=None:
        print(p.val)
        p = p.next