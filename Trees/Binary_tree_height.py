#How to check the depth of a binary tree

def maxdepth(node):
    if node is None:
        return 0
        
    #Check for height on the left
    left = maxdepth(node.left)
        
    #check for height on the right#
    right = maxdepth(node.right)
        
    return max(left,right) + 1
    
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
root = Node(10)
root.left = Node(5)
root.right = Node(6)
root.right.left = Node(8)
root.right.right = Node(7)
root.right.right.right = Node(4)
print (maxdepth(root))

                
                    
                        
                    
                    
            