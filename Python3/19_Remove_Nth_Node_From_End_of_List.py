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
    # Time Complexity:
    # Worst Case: O(n + n) = O(2n)
    # Asytompic Case: O(n)
    # Best Case: O(n)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        
        head.prev = None
        curr = head.next
        pre = head
        length = 1
        while curr is not None:
            curr.prev = pre
            pre = curr
            curr = curr.next
            length += 1
            
        if length == n:
            if length == 1:
                return None
            else:
                head.next.prev = None
                return head.next
        
        i = 1
        while i <= n:
            pre = pre.prev
            i += 1
            
        pre.next = pre.next.next
        
        return head