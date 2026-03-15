# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        b = 0
        c = l1
        d = l2
        while c:
            a+=1
            c = c.next
        while d:
            d= d.next
            b+=1
        
        if a>b:
            l2,l1 = l1,l2
        
        ca = 0
        nh = l2
        while l2:
            if not l1:
                l2.val+=ca
                if l2.val >= 10:
                    ca = 1
                    l2.val%=10
                else:
                    ca = 0
                
                if not l2.next:
                    if ca != 0:
                        l2.next = ListNode(ca)
                        break
                l2 = l2.next
                continue
            else:
                l2.val+=ca+l1.val
                if l2.val >= 10:
                    ca = 1
                    l2.val%=10
                else:
                    ca = 0
                if not l2.next:
                    if ca != 0:
                        l2.next = ListNode(ca)
                        break
                l2 = l2.next
                l1 = l1.next
        
        return nh
