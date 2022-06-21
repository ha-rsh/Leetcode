# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tail1 = headA
        tail2 = headB
        while (tail1 != tail2):
            if tail1 == None:
                tail1 = headB
            else:
                tail1 = tail1.next


            if tail2 == None:
                tail2 = headA
            else:
                tail2 = tail2.next

    
        return tail1
            