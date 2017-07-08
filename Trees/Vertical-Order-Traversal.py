#Vertical order traversal of a binary tree #
# http://www.geeksforgeeks.org/print-binary-tree-vertical-order/

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
        
def findminmax(node,min,max,distance):

    if node is None:
        return
        
    #The min and max distance would anyways be updated , this is just keeping the provision on for left and right
    if distance < min[0]:
        min[0] = distance
    if distance > max[0]:
        max[0] = distance
        
    findminmax(node.left,min,max,distance - 1)
    findminmax(node.right,min,max,distance + 1)
    
    
def printverticalline(node,line_no,distance):
    if node is None:
        return
        
    if distance == line_no:
        print (node.data)
        
    printverticalline(node.left,line_no,distance - 1)
    printverticalline(node.right,line_no,distance + 1)
    
        
def verticalOrder(root):
    min = [0]
    max = [0]
    findminmax(root,min,max,0)
    
    print ("Minimum and maximum distance is: ",min[0],max[0])
    
    for line_no in range(min[0],max[0]+1):
        printverticalline(root,line_no,0)
        
        
        
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)

print ("Vertical order traversal is as follows:")
verticalOrder(root)