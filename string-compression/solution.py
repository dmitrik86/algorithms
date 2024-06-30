class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def getStringLength(prevLetter, num, idx, k):
            if idx == n:
                return 0
            if k == 0:
                if s[idx] == prevLetter:
                    return getStringLength(s[idx], num + 1, idx + 1, k) + (1 if num == 1 or num == 9 or num == 99 else 0)
                else:
                    return getStringLength(s[idx], 1, idx + 1, k) + 1
            if prevLetter == None:
                return min(getStringLength(s[idx], num + 1, idx + 1, k) + 1, getStringLength(None, num, idx + 1, k - 1))
            if s[idx] == prevLetter:
                return min(getStringLength(s[idx], num + 1, idx + 1, k) + (1 if num == 1 or num == 9 or num == 99 else 0), 
                    getStringLength(prevLetter, num, idx + 1, k - 1))
            return min(getStringLength(s[idx], 1, idx + 1, k) + 1, 
                getStringLength(prevLetter, num, idx + 1, k - 1))
        return getStringLength(None, 0, 0, k)