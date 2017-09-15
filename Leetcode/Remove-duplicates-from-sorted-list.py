# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(0)
        newnode = newhead
        data = set()
        node = head
        while node != None:
            value = node.val
            if value not in data:
                newnode.next = ListNode(value)
                newnode = newnode.next
                data.add(value)
            else:
                node = node.next
        return newhead.next