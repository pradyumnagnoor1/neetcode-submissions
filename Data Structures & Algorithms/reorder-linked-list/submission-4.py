# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # slow finds the middle, fast moves twice as fast
        slow = head
        fast = head

        # when fast hits the end, slow is at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # second starts after the middle
        second = slow.next

        # cut list into two halves, and set prev for reversing
        prev = slow.next = None

        # reverse the second half
        while second:
            temp = second.next      # save next node
            second.next = prev      # reverse pointer
            prev = second           # move prev forward
            second = temp           # move second forward

        # first half starts at head
        first = head

        # reversed second half starts at prev
        second = prev

        # merge first and second halves
        while second:
            temp1 = first.next      # save next first-half node
            temp2 = second.next     # save next second-half node

            first.next = second     # first points to second
            second.next = temp1     # second points back to first half

            first = temp1           # move first forward
            second = temp2          # move second forward