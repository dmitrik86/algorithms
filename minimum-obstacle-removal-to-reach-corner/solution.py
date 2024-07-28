class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        graph = defaultdict(list)
        for row in range(m):
            for col in range(n):
                if row > 0:
                    graph[(row, col)].append((row - 1, col))
                if col > 0:
                    graph[(row, col)].append((row, col - 1))
                if row + 1 < m:
                    graph[(row, col)].append((row + 1, col))
                if col + 1 < n:
                    graph[(row, col)].append((row, col + 1))
        visited = defaultdict(int)
        visited[(0, 0)] = grid[0][0]
        heap = [[grid[0][0], 0, 0]]
        while heap:
            currentCost, row, col = heapq.heappop(heap)
            for neighbor in graph[(row, col)]:
                if (neighbor[0], neighbor[1]) not in visited \
                    or visited[(neighbor[0], neighbor[1])] > currentCost + grid[neighbor[0]][neighbor[1]]:
                    visited[(neighbor[0], neighbor[1])] = currentCost + grid[neighbor[0]][neighbor[1]]
                    heapq.heappush(heap, [visited[(neighbor[0], neighbor[1])], neighbor[0], neighbor[1]])
        return visited[(m - 1, n - 1)]