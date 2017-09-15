# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = self.find_min_depth(root)
        return depth
    
    def find_min_depth(self,node):
        if node is None:
            return 0
        if node.left is None:
            return self.find_min_depth(node.right) + 1
        if node.right is None:
            return self.find_min_depth(node.left) + 1
        
        return min(self.find_min_depth(node.left),self.find_min_depth(node.right)) + 1