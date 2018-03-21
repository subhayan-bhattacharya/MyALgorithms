# https://www.geeksforgeeks.org/lucky-alive-person-circle/

class Node:
    def __init__(self,node):
        self.data = node
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self,data):
        new = Node(data)
        if self.head is None:
            new.next = new
            self.head = new
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new
            new.next = self.head
            
    def deladjacent(self):
        temp = self.head
        print "head is :",temp.data
        while temp.next != temp:
            killed = temp.next
            temp.next = killed.next
            temp = temp.next
        print temp.data
                
                
if __name__ == "__main__":
    c = CircularLinkedList()
    n = 100
    for i in range(1,n+1):
        c.push(i)
    c.deladjacent()
    
        