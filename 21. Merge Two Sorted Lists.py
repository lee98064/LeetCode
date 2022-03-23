# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.findMin(list1, list2)
    
    def findMin(self,n1, n2):
        if(n1 == None):
            return n2
        
        if(n2 == None):
            return n1
        if(n1.val < n2.val):
            n1.next = self.findMin(n1.next, n2)
            return n1
        else:
            n2.next = self.findMin(n1, n2.next)
            return n2
        