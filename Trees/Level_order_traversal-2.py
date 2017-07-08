#http://www.geeksforgeeks.org/print-level-order-traversal-line-line/


class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def print_level_order_newline(root):
    if root == None:
        return
        
    queue = []
    
    queue.append(root)
    queue.append("newline")
    
    while len(queue) > 0:
        node = queue.pop(0)
        if node == "newline":
            print ("\n",end="")
            if len(queue) > 0:
                queue.append("newline")
            continue
        else:
            print (node.data,end = " ")
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
              
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(9)
root.left.right.left = Node(7)
root.left.right.right = Node(8)
root.left.right.right.left = Node(10)
root.left.right.right.right = Node(11)


print_level_order_newline(root)