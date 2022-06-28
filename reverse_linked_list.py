# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l_list = []
        while head is not None:
            l_list.append(head.val)
            head = head.next
            
        l_list = l_list[::-1]
        node = dummy = ListNode(0)
        for i in l_list:
            newnode = ListNode(i)
            node.next = newnode
            node = newnode
            
        return dummy.next