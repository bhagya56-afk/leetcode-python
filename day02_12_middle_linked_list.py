# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        count=0
        new=head
        while new:
            count+=1
            new=new.next
        i=0
        while i!=count//2:
            head=head.next
            i+=1
        return head

        