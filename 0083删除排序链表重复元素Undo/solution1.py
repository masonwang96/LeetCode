# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head.next is None:
        #     return head
        p = head
        while p.next and p:
            if p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    head = Solution().deleteDuplicates(l1)
    while head.next:
        print(head.val)
        head = head.next
    print(head.val)
    l2 = ListNode(1)
    l2.next = ListNode(1)
    l2.next.next = ListNode(2)
    l2.next.next.next = ListNode(3)
    l2.next.next.next.next = ListNode(3)
    head = Solution().deleteDuplicates(l2)
    while head.next:
        print(head.val)
        head = head.next