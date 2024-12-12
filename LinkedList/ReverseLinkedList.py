class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
    def printlist(self):
        li = []
        current = self.head
        while current:
            li.append(current.value)
            current = current.next
        return li
    def reverseList(self):
        previous,current = None,self.head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

arr = LinkedList()
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
print(arr.printlist())
arr.reverseList()
print(arr.printlist())