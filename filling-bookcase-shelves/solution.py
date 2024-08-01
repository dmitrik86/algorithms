class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        @cache
        def minHeight(idx, rowHeight, rowWidth):
            if idx == n:
                return 0
            if rowWidth + books[idx][0] <= shelfWidth:
                if rowHeight < books[idx][1]:
                    return min(minHeight(idx + 1, books[idx][1], rowWidth + books[idx][0]) + books[idx][1] - rowHeight, 
                        minHeight(idx + 1, books[idx][1], books[idx][0]) + books[idx][1])
                else:
                    return min(minHeight(idx + 1, rowHeight, rowWidth + books[idx][0]), 
                        minHeight(idx + 1, books[idx][1], books[idx][0]) + books[idx][1])
            return minHeight(idx + 1, books[idx][1], books[idx][0]) + books[idx][1]
        return minHeight(0, 0, 0)