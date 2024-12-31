# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:      
        dum = ListNode()  
        l = dum
        
        while list1 and list2:
            if list1.val < list2.val:
                l.next = list1
                list1, l = list1.next, list1
            else:
                l.next = list2
                list2, l = list2.next, list2

        if list1 or list2:
            l.next = list1 if list1 else list2
        return dum.next
    
#0ms 16.74Mb (100.00% 5.76%)