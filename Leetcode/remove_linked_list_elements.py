# https://leetcode.com/problems/remove-linked-list-elements/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head

        while head.val == val:
            if head.next == None:
                return None
            else:
                head = head.next

        prev = head
        node = head.next
        while node != None:
            if node.val == val:
                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next
        return head