# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            temp.next = ListNode(total % 10)
            temp = temp.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
    
# Solution.addTwoNumbers(Solution, ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
# 9ms 12.52Mb