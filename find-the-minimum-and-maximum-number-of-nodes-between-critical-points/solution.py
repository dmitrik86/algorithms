class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return [-1, -1]
        prevNode, currentNode = head, head.next
        currentIndex = 1
        critical = []
        while currentNode.next:
            if prevNode.val < currentNode.val > currentNode.next.val:
                critical.append(currentIndex)
            if prevNode.val > currentNode.val < currentNode.next.val:
                critical.append(currentIndex)
            prevNode = currentNode
            currentNode = currentNode.next
            currentIndex += 1
        if len(critical) < 2:
            return [-1, -1]
        maxDistance = critical[-1] - critical[0]
        minDistance = float('inf')
        for i in range(1, len(critical)):
            minDistance = min(minDistance, critical[i] - critical[i - 1])
        return [minDistance, maxDistance] if minDistance != float('inf') else [maxDistance, maxDistance]