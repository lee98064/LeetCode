# notworking wait to fix
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, val):
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        self.size += 1

    def sort(self):
        for i in range(self.size,0,-1):
            now = self.head
            prev = self.head
            for j in range(0, i-1, 1):
                if(now.val > now.next.val):
                    tmp = now.next
                    now.next = tmp.next
                    tmp.next = now

                    if(now == self.head):
                        self.head = tmp
                        prev = tmp
                    else:
                        prev.next = tmp
                        prev = prev.next
                else:
                    now = now.next
                    if(j != 0):
                        prev = prev.next

    def to_list(self):
        result = []
        i = self.head
        while(i != None):
            result.append(i.val)
            i = i.next
        return result

class Solution:
    def mergeTwoLists(self, list1, list2):
        linklist = SingleLinkList()
        for i in list1 + list2:
            linklist.append(i)
        linklist.sort()
        print(linklist.to_list())


a = Solution().mergeTwoLists([1,2,4],[1,3,4])