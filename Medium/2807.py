# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cache = head
        while head and head.next:
            nxt = head.next.val
            head.next = ListNode(self.gcd(head.val, nxt), head.next)
            head = head.next.next
        return cache

# 37ms 19.52Mb