# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        list2 = s.next
        prev = s.next = None

        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp

        list1, list2 = head, prev
        while list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2