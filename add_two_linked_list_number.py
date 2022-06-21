# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        num1 = ""
        num2 = ""
        while(l1 != None):
            num1 += str(l1.val)
            l1 = l1.next
        while(l2 != None):
            num2 += str(l2.val)
            l2 = l2.next
            
        num1 = str(int(num1[::-1])+int(num2[::-1]))[::-1]
        print(num1)
        cur = dummy = ListNode(0)
        for d in num1:
            cur.next = ListNode(int(d))
            cur = cur.next
        return dummy.next