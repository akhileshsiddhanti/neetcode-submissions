# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        current = head

        if head is None:
            return head
        
        while current:
            l += 1
            current = current.next

        if n == l:
            current = head.next
            head.next = None
            return current

        # Remove (l-n+1)th node
        current = head
        prev = None
        i = 0

        while i < (l-n) and current is not None: # i=0,i=1 if n=l-1 then l-n+1 = 2
            prev = current
            current = current.next
            i += 1
        

        if n < l:
            prev.next = current.next
        elif n==l:
            prev.next = None
        
        return head



        