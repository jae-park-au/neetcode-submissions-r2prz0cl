# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        while cur:
            cur = cur.next
            length += 1

        temp_head = ListNode()
        temp_head.next = head
        cur = temp_head
        pos = 0
        while cur:
            if pos == (length - n):
                if cur.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
                break

            cur = cur.next
            pos += 1

        return temp_head.next
