# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = head
        cur = head.next
        last = head.next.next

        pre.next = last
        cur.next = last.next
        last.next = cur
        print (head.val,head.next.val,head.next.next.val,head.next.next.next.val)

        

if __name__ == "__main__":
    a = Solution()
    
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(4)
    b.next = c
    c.next = d
    d.next = e

    a.oddEvenList(b)



