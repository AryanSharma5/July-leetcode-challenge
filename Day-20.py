# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if head:
            curr = head
            prev = None
            while curr:
                while curr and curr.val != val:
                    prev = curr
                    curr = curr.next
                if not curr:
                    break
                prev.next = curr.next
                curr = prev.next
            return head
        return None