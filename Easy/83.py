
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
                continue
            head = head.next
        return res
    
#0ms 11.70Mb (100.00% 63.56%)