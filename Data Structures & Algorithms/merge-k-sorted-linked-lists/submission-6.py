# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop
        
        h = []
        j=0
        for i in range(len(lists)):
            if lists[i] is not None:
                heappush(h, (lists[i].val, i+j, lists[i]))
                lists[i] = lists[i].next
                j+=1

        current = None
        start = None
        
        while len(h) > 0:
            val, _, node1 = heappop(h)
            
            if current is None:
                current = node1
                start = current
            else:
                current.next = node1
                current = current.next
            
            if node1.next:
                heappush(h, (node1.next.val, i+j, node1.next))
                j+=1

        return start
            

