# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        root = ListNode()
        currentNode = ListNode()
        root.next = currentNode
        while l1 != None and l2 != None:
            
            if l1.val <= l2.val:
                currentNode.next = l1
                currentNode = currentNode.next
                l1 = l1.next
                
            else:
                currentNode.next = l2
                currentNode = currentNode.next
                l2 = l2.next
                
            
                
        if l1 == None:
            while l2 != None:
                currentNode.next = l2
                currentNode = currentNode.next
                l2 = l2.next
            
        elif l2 == None:
            while l1 != None:
                currentNode.next = l1
                currentNode = currentNode.next
                l1 = l1.next
            
        root = root.next.next
        return root