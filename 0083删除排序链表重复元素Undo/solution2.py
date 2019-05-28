# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        p = l1
        q = l1
        l = ListNode(-1)
        res = l
        while p.next:
            if p.val < q.val:
                l.next = p
                l = l.next
                p = p.next
            elif p.val > q.val:
                l.next = q
                l = l.next
                q = q.next
            else:
                l.next = p
                l = l.next
                l.next = q
                l = l.next
                p = p.next
                q = q.next
        while res.next:
            print(res.val)
            res = res.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print(Solution().mergeTwoLists(l1, l2))
