# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        for i in range(len(lst)):
            if lst[i]!=lst[len(lst)-1-i]:
                return False
        return True
        