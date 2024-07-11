class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''
        stack = []
        for lt in s:
            if lt != ')':
                stack.append(lt)
                continue
            reverse = []
            while stack:
                lt = stack.pop()
                if lt != '(':
                    reverse.append(lt)
                    continue
                stack += reverse
                break
        return ''.join(stack)