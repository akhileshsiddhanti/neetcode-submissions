# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        prev = None
        root = None

        while current is not None:
            next = current.next
            if next is None:
                root = current
            current.next = prev
            prev = current
            current = next
        return root


            