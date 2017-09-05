# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isMirror(root.left,root.right)
        
    def isMirror(self,x,y):
        if x == None and y == None:
            return True
        elif x != None and y != None:
            if x.val != y.val:
                return False
        
            if self.isMirror(x.left,y.right):
                if self.isMirror(x.right,y.left):
                    return True

        return False