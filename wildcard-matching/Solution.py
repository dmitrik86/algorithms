class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        @cache
        def match(s_idx, p_idx):
            if s_idx == n and p_idx == m:
                return True
            if s_idx < n and p_idx == m:
                return False
            if s_idx == n and p_idx < m:
                while p_idx < m and p[p_idx] == '*':
                    p_idx += 1
                return p_idx == m
            if s[s_idx] == p[p_idx] or p[p_idx] == '?':
                return match(s_idx + 1, p_idx + 1)
            if p[p_idx] == '*':
                return match(s_idx + 1, p_idx + 1) or match(s_idx + 1, p_idx) or match(s_idx, p_idx + 1)
            return False
        return match(0, 0)