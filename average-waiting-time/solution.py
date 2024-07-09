class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        if n == 0:
            return 0
        waitingTime = []
        queue = deque()
        queue.append(customers[0])
        idx = 1
        currentTime = customers[0][0]
        while queue:
            time, preparingTime = queue.popleft()
            currentTime += preparingTime
            waitingTime.append(currentTime - time)
            while idx < n and currentTime >= customers[idx][0]:
                queue.append(customers[idx])
                idx += 1
            if len(queue) == 0 and idx < n:
                queue.append(customers[idx])
                currentTime = customers[idx][0]
                idx += 1
        return sum(waitingTime) / n