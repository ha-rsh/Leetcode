# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        d = {}
        i = 0
        while tail is not None:
            if tail in d: return tail
            else: 
                d[tail] = i
                i += 1
            tail = tail.next
        