# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode(0, None)
        ansTmp = ans
        head = head.next
        temp = 0
        while head:
            if head.val == 0:
                ansTmp.next = ListNode(temp)
                ansTmp = ansTmp.next
                temp = 0
            else:
                temp += head.val
            
            head = head.next
        return ans.next
    
# 871ms 197.5Mb