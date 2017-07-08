# boolean isBST(Node root, int min, int max)
# {
 # if root == None:
    # return True
    
 # if root.data <= min or roo.data > max:
    # return False
    
 # return isBST(node.left,min,node.data) && isBST(node.right,root.data,max)
# }



INT_MAX = 4294967296
INT_MIN = -4294967296


def isBST(node,min,max):
    if node == None:
        return True
    
    if node.data < min or node.data > max:
        return False
    
    return isBST(node.left,min,node.data - 1) and isBST(node.right,node.data + 1,max)
    
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
                
                
def check_binary_search_tree_(root):
    if isBST(root,INT_MIN,INT_MAX):
        return True
    else:
        return False
       

    
        
                
if __name__ == '__main__':
    INT_MAX = 4294967296
    INT_MIN = -4294967296
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
    
    print (check_binary_search_tree_(node))

            