# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        cNode1 = l1
        cNode2 = l2
        carry = 0
        
        while cNode1!=None or cNode2!=None:
            
            cNode2.val += cNode1.val + carry
            carry = 0
            
            if cNode2.val > 9:
                cNode2.val -= 10
                carry = 1
                
            if(cNode2.next == None and cNode1.next == None):
                if carry == 1:
                    cNode2.next = ListNode(1)
                break
            
            if cNode1.next == None:
                cNode1.next = ListNode()
                
            if cNode2.next == None:
                cNode2.next = ListNode()
            
            cNode1 = cNode1.next
            cNode2 = cNode2.next
            
        return l2