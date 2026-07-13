class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkList:

    def __init__(self, head=None):
        self.head = head
    
    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        return
    
    def makeListFromArr(self, arr):
        for val in arr:
            self.append(val)
        return 
    
    def printlist(self):
        temp = self.head

        while temp is not None:
            print(temp.val, end='->')
            temp = temp.next
        
        return
