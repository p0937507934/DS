from singledlinkedlist import SingleLinkedList
class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList(SingleLinkedList):
    
    def __init__(self):
        super().__init__()
        self.head = None
    
    def add(self,val):
        """
        add Node in the front.
        :params
        val:Node value.
        """
        n = Node(val)
        if  not self.head :
            self.head = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
    
    def append(self,val):

        node = Node(val)
        if self.is_empty():
            self.head = node
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = node
        node.prev = cur


    def insert(self,pos,val):
        """
        插入指定位置
        :params
        pos:start from 0
        val:Node val
        """
        if pos<=0:
            self.add(val)
        elif pos > (self.length - 1):
            self.append(val)
        else:
            cur = self.head
            while pos != 0:
                pos = pos - 1
                cur = cur.next
            node = Node(val)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
        



        



d = DoubleLinkedList()
d.add(1)
d.add(2)
d.travel()
print(d.head.next.prev.val)
