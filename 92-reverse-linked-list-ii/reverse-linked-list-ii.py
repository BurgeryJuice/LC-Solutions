# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lop = False
        lvn = None
        curr = head
        for i in range(left-1):
            if i == left-2:
                lop = True
                lvn = curr
                curr = curr.next
                break
            curr = curr.next
            

        pre = None
        
        oh = curr
        for i in range(right-left+1):
            nex = curr.next
            curr.next = pre
            pre = curr
            curr = nex
        if not lop:
            head = pre
            oh.next = curr
            return head

        lvn.next = pre
        oh.next = curr
        return head
        
        
        