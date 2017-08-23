# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        newlist = root
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                new = ListNode(l1.val)
                newlist.next = new
                newlist = new
                l1 = l1.next
            elif l2.val < l1.val:
                new = ListNode(l2.val)
                newlist.next = new
                newlist = new
                l2 = l2.next
            else:
                new1 = ListNode(l1.val)
                new2 = ListNode(l2.val)
                newlist.next = new1
                newlist = new1
                newlist.next = new2
                newlist = new2
                l1 = l1.next
                l2 = l2.next
        if l1 == None and l2 != None:
            newlist.next = l2
        elif l2 == None and l1 != None:
            newlist.next = l1
            
        return root.next