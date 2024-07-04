class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        node = head
        while node and node.next:
            if node.next.val == 0:
                node.next = node.next.next
                node = node.next
                continue
            node.val += node.next.val
            node.next = node.next.next
        return head