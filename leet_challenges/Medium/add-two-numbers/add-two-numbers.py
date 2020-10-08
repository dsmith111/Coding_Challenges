# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        arr1 = []
        arr2 = []
        temp1 = l1
        temp2 = l2
        
        while((temp1 != None) or (temp2 != None)):

            if(temp1 == None):
                arr1.insert(0, 0)
                arr2.insert(0, temp2.val)
                temp2 = temp2.next
            
            elif(temp2 == None):
                arr1.insert(0, temp1.val)
                arr2.insert(0, 0)
                temp1 = temp1.next
                
            else:
                arr1.insert(0, temp1.val)
                arr2.insert(0, temp2.val)
                temp1 = temp1.next
                temp2 = temp2.next
                
        arr1 = list(map(lambda digit: str(digit), arr1))
        arr2 = list(map(lambda digit: str(digit), arr2))                
        num1 = int(''.join(arr1))
        num2 = int(''.join(arr2))

        num3 = num1 + num2
 
        num3 = str(num3)
        
        first = True
        for digit in num3:
            current_val = int(digit)
            
            if(first):
                root = ListNode(current_val)
                first = False
            
            else:
                root = ListNode(current_val, root)
                
        return root