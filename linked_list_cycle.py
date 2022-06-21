# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = head
        s = {}
        while tail is not None:
            if tail in s: return True
            else: s[tail] = 1
            tail = tail.next
        return False
            