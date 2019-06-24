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
    # Time Complexity: O(n)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        n = head
        prev = head
        while n != None:
            if n.val == prev.val:
                prev.next = n.next
                n = n.next
            else:
                prev = n
                n = n.next
        return head
            