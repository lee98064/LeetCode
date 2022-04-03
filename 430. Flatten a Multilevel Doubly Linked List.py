
# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        a = self.dfs(head)
        while(a != None and a.prev != None):
            a = a.prev
        return a

    def dfs(self,h):
        if(h==None): return None

        child = h.child
        next = h.next
        h.child = None

        if(child == None and next == None):
            return h
        elif(child != None and next == None):
            h.next = child
            child.prev = h
            childEnd = self.dfs(child)
            return childEnd
        elif(child == None and next != None):
            nextEnd = self.dfs(next)
            return nextEnd
        else:
           h.next = child
           child.prev = h
           childEnd = self.dfs(child)
           childEnd.next = next
           next.prev = childEnd
           return self.dfs(next)




        


    # def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     now = head
    #     node_list = []
        
    #     while(now.next != None):
    #         node_list.append(now) 
    #         now = now.next
        
    #     i = 0
    #     while(i > len(node_list) - 1):

    #         if(node_list[i].child != None):
    #             temp = self.flatten(node_list[i])
    #             node_list.insert(i,temp)
    #             node_list[i].next = node_list[i + 1]
    #             node_list[i + 1].prev = node_list[i]
    #             i = i + len(temp) - 1
    #             if(i + 1 > len(node_list) - 1):
    #                 node_list[i] = None
    #             else:
    #                 node_list[i].next = node_list[i + 1]
    #             i += 1
    #         else:
    #             i += 1
        
    #     result = None
    #     for i in node_list:
    #         result = i
    #         result.child = None
    #         result = result.next

    #     return(result)