# Recursive calls in Binary search tree #
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.data < data:
            #print (data," is more than: ",self.data)
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        elif self.data > data:
            #print (data," is less than: ",self.data)
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
                
    def lookup(self,data,parent=None):
        if self.data == data:
            return self, parent
        else:
            if self.data > data:
                if self.left == None:
                    return None, None
                else:
                    return self.left.lookup(data,self)
            else:
                if self.right == None:
                    return None, None
                else:
                    return self.right.lookup(data,self)
                    

    def delete(self,data):
        (node,parent) = self.lookup(data)
        if node != None:
            if node.left == None and node.right == None:
                print ("Deleting leaf node!")
                if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None
                    del node
                else:
                    self.data = None
            elif node.left == None or node.right == None:
                if parent:
                    if node.left == None:
                        print ("Node has only right node")
                        if parent.right == node:
                            parent.right = node.right
                        else:
                            parent.left = node.right
                    else:
                        print ("Node has only left node")
                        if parent.right == node:
                            parent.right = node.left
                        else:
                            parent.left = node.left
                    del node
                else:
                    print ("This is the root node")
                    if node.left == None:
                        # Root node has only right node #
                        node.data = node.right.data
                        node.left = node.right.left
                        node.right = node.right.right
                    else:   
                        # Root node has only left node #
                        node.data = node.left.data
                        node.left = node.left.left
                        node.right = node.left.right
            elif node.left != None and node.right != None:
                print ("Node has both left and right nodes!")
                parent = node
                successor = node.right
                while successor.left != None:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                parent.right = successor.right
                del successor
        else:
            print ("There is no such node to be deleted!")
            
    def print_inorder(self):
    # printing tree in-order #
    # Left-root-right (produces ascending order keys)
        if self.left:
            self.left.print_inorder()
        print (self.data)
        if self.right:
            self.right.print_inorder()
            
    def print_preorder(self):
    # printing tree pre-order #
    # Root-Left-right #
        print (self.data)
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()
            
        
    def print_postorder(self):
    # Left-right-root #
    # printing tree post-order #
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print (self.data)
        
                    
            
        

if __name__ == '__main__':
    node = Node(7)
    node.insert(4)
    node.insert(2)
    node.insert(3)
    node.insert(6)
    node.insert(5)
    node.insert(12)
    node.insert(9)
    node.insert(8)
    node.insert(11)
    node.insert(19)
    node.insert(15)
    node.insert(20)
    
    # (check,parent) = node.lookup(10)
    # if check != None:
        # print ("Found 10 and its parent is:",parent.data)
    # else:
        # print ("10 not found")
   
    # (check,parent)= node.lookup(6)
    # if check != None:
        # print ("Found 6 and its parent is:",parent.data)
    # else:
        # print ("6 not found")
    
    # node.delete(8)
    node.print_inorder()
    print ("Changing printing order")
    node.print_preorder()
    print ("Changing again !")
    node.print_postorder()
    

                    
              
         