# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        from collections import deque
        
        first = head
        last = head

        st = deque()
        
        while last is not None:
            st.append(last)
            last = last.next

        while len(st) > 1:
            last  = st.pop()
            first = st.popleft()
            
            second = st[0] if st else None
            
            first.next = last
            last.next = second

        if len(st) == 1:
            st[0].next = None
