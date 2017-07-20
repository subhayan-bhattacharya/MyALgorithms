#Leetcode problem of adding two numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        final = dummyhead
        carry = 0
        p = l1
        q = l2
        
        while q != None or p != None:
            if p == None:
                x = 0
                y = q.val
                q = q.next
            elif q == None:
                x = p.val
                y = 0
                p = p.next
            else:
                x = p.val
                y = q.val
                p = p.next
                q = q.next
            sum = x + y + carry
            carry = sum // 10
            toadd = sum % 10
            final.next = ListNode(toadd)
            final = final.next
        if carry != 0:
            final.next = ListNode(carry)
        return dummyhead.next