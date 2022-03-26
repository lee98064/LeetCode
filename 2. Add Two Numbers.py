# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = l1
        arr1 = ""
        while(i != None):
            arr1 += str(i.val)
            i = i.next
            
        i = l2
        arr2 = ""
        while(i != None):
            arr2 += str(i.val)
            i = i.next
        
        ans = int(arr1[::-1]) + int(arr2[::-1])
        
        result = ListNode()
        now = result
        for i in str(ans)[::-1]:
            now.next = ListNode(i)
            now = now.next
            
        return result.next