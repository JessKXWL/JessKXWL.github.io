# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


class ListNode(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Chain(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def get_length(self):
        p = self.head
        while p!=None:
            self.length = self.length + 1
            p = p.next

    def travel(self):
        p = self.head
        while p != None:
            if p.next == None:
                print("{value}".format(value=p.value))
            else:
                print("{value} -> ".format(value = p.value), end='')
            p = p.next

    def append(self, value):
        new = ListNode(value)
        if self.is_empty():
            self.head = new

        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = new
        self.length = self.length + 1


    def insert(self, pos, value):
        new = ListNode(value)
        if self.is_empty():
            print("链表为空")
        if pos>self.length or pos<0:
            print("插入位置不合法")
            return
        if pos == 1:
            new.next = self.head
            self.head = new
            self.length = self.length + 1
            return

        # 第一个位置是1
        p = self.head
        count = 1
        while count != pos-1:
            count = count + 1
            p = p.next
        new.next = p.next
        p.next = new
        self.length = self.length + 1

    def remove(self, value):
        p = self.head
        q = None
        while p.value!=value:
            q = p
            p = p.next
        q.next = q.next.next
        self.length = self.length - 1
        return p.value

    def delete(self, pos):
        if self.is_empty():
            print("链表为空")
        if pos>self.length or pos<0:
            print("超出边界")
            return
        if pos == 1:
            self.head = self.head.next
            self.length = self.length - 1
            return
        p = self.head
        q = None
        count = 1
        while count != pos - 1:
            count = count + 1
            q = p
            p = p.next

        q.next = q.next.next
        self.length = self.length - 1
        return p.value


    def seach(self, value):
        pass

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p = l1.head
        list1 = []
        while p!=None:
            list1.append(p.value)
            p = p.next
        p = l2.head
        list2 = []
        while p !=None:
            list2.append(p.value)
            p = p.next
        num1 = ''.join(str(i) for i in list1[::-1])
        num2 = ''.join(str(i) for i in list2[::-1])
        num3 = str(int(num1) + int(num2))[::-1]

        chain1 = Chain()
        chain1.head = ListNode(int(num3[0]))
        print(len(num3))
        for i in (1,len(num3)-1):
            chain1.append(int(num3[i]))
        return chain1


if __name__ == '__main__':
    str1 = input()
    flag = 0

    l1 = Chain()
    l2 = Chain()

    for i in str1:
        if i == '+':
            flag = 1
        if i.isdigit() and flag == 0:
            l1.append(i)
        if i.isdigit() and flag == 1:
            l2.append(i)
    solu = Solution()
    result = solu.addTwoNumbers(l1, l2)
    result.travel()