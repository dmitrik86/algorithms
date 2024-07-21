class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowInEdges = defaultdict(int)
        rowOutEdges = defaultdict(list)
        colInEdges = defaultdict(int)
        colOutEdges = defaultdict(list)
        for node1, node2 in rowConditions:
            rowInEdges[node2] += 1
            rowOutEdges[node1].append(node2)
        for node1, node2 in colConditions:
            colInEdges[node2] += 1
            colOutEdges[node1].append(node2)
        queue = deque()
        for node in range(1, k + 1):
            if rowInEdges[node] == 0:
                queue.append(node)
        rowOrder = defaultdict(int)
        while queue:
            node = queue.popleft()
            rowOrder[node] = len(rowOrder)
            for child in rowOutEdges[node]:
                rowInEdges[child] -= 1
                if rowInEdges[child] == 0:
                    queue.append(child)
        if len(rowOrder) < k:
            return []
        queue = deque()
        for node in range(1, k + 1):
            if colInEdges[node] == 0:
                queue.append(node)
        colOrder = defaultdict(int)
        while queue:
            node = queue.popleft()
            colOrder[node] = len(colOrder)
            for child in colOutEdges[node]:
                colInEdges[child] -= 1
                if colInEdges[child] == 0:
                    queue.append(child)
        if len(colOrder) < k:
            return []
        grid = [[0 for _ in range(k)] for _ in range(k)]
        for node in rowOrder:
            grid[rowOrder[node]][colOrder[node]] = node
        return grid