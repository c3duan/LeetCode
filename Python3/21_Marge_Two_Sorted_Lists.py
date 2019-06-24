# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Time Complexity: O(min(m,n))
    # Note: m = length of l1, n = list of l2
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        l = ListNode(0)
        start = l
        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                l.val = l2.val
                l.next = ListNode(0)
                l = l.next
                l2 = l2.next
                
            elif l1.val < l2.val:
                l.val = l1.val
                l.next = ListNode(0)
                l = l.next
                l1 = l1.next
                
        if l1 != None:
            l.val = l1.val
            l.next = l1.next
            
        if l2 != None:
            l.val = l2.val
            l.next = l2.next
            
        return start