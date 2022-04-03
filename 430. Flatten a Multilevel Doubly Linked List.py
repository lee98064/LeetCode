
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



class Solution2:

    def node_to_list(self,head):
        if(head == None): return []
        node_list = []
        now = head
        while(now != None):
            node_list.append(now) 
            now = now.next
        return node_list

    def link_list_to_node(self,head):
        result = None
        for i in range(0, len(head),1):
            result = head[i]
            result.child = None
            if(i == 0):
                result.prev = None
            else:
                result.prev = head[i - 1]

            if(i == len(head) - 1):
                result.next = None
                break
            else:
                result.next = head[i + 1]
            result = result.next

        return result

    def reverse_node(self, head):
        while(head != None and head.prev != None):
            head = head.prev

        return(head)

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        a = self.node_to_list(head)
        a = self.process(a)
        a = self.link_list_to_node(a)
        a = self.reverse_node(a)
        return a

    def process(self, head):
        node_list = head
        final_list = []

        for i in node_list:
            final_list.append(i)
            if(i.child != None):
                final_list += self.process(self.node_to_list(i.child))
        return final_list