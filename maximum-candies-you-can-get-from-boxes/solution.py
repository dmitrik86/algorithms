class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque()
        result = 0
        allowedKeys = set()
        for box in initialBoxes:
            queue.append([box, status[box]])
        while queue:
            newBox = False
            closed = []
            for _ in range(len(queue)):
                box, boxStatus = queue.popleft()
                if boxStatus == 1 or box in allowedKeys:
                    result += candies[box]
                    candies[box] = 0
                    for key in keys[box]:
                        allowedKeys.add(key)
                        newBox = True
                    for contained in containedBoxes[box]:
                        queue.append([contained, status[contained]])
                        newBox = True
                else:
                    closed.append([box, 1 if box in allowedKeys else 0])
            if newBox:
                queue += closed
        return result