# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition( head, x) :
        after,before = ListNode(0),ListNode(0)
        after_curr,before_curr = after,before

        while head :
            if head.val < x:
                before_curr.next,before_curr = head,head
            else:
                after_curr.next,after_curr = head,head
            head=head.next
        after_curr.next = None
        before_curr.next = after.next
        return before.next