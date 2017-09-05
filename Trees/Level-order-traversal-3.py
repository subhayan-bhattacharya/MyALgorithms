class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def traverse_inorder(root):
    queue = [root]
    while len(queue) != 0:
        element = queue[0]
        del queue[0]
        
        print (element.data)
        if element.left != None:
            queue.append(element.left)
            
        if element.right != None:
            queue.append(element.right)
        
        
        
if __name__ == "__main__":
        
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(7)
    root.left.right.right = Node(8)
    root.right.right = Node(6)
    root.right.right.left = Node(9)
    
    traverse_inorder(root)
    

