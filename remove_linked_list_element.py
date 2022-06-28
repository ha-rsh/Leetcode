# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = []
        while head is not None:
            if head.val != val: 
                ans.append(head.val)
            head = head.next
                
        node = dummy = ListNode(0)
        for i in ans:
            newnode = ListNode(i)
            node.next = newnode
            node = newnode
            
        return dummy.next