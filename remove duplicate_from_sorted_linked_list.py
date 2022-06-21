# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        temp = head
        while temp is not None:
            values.append(temp.val)
            temp = temp.next
            
        values = set(values)
        values = list(values)
        values.sort()
        node = dummy = ListNode(0)
        for ele in values:
            newnode = ListNode(ele)
            node.next = newnode
            node = newnode
            
        return dummy.next