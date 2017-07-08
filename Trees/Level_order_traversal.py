class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def print_level_order(root):
    if root == None:
        return
        
    queue = []
    
    queue.append(root)
    
    while len(queue) > 0:
        print (queue[0].data)
        node = queue.pop(0)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
        
        
        
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)

print_level_order(root)
        
