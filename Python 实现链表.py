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

if __name__ == '__main__':
    chian = Chain()
    chian.append('a')
    chian.append('b')
    chian.append('c')
    chian.append('d')
    chian.append('e')
    chian.append('f')
    chian.append('g')
    chian.append('h')
    chian.append('i')
    chian.travel()
    chian.insert(1, 'm')
    chian.travel()
    chian.delete(1)
    chian.travel()
    chian.remove('b')
    chian.travel()