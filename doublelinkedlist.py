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
        



d = DoubleLinkedList()
d.add(1)
d.add(2)
d.travel()
print(d.head.next.prev.val)
