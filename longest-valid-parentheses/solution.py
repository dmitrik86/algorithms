class Solution:
    def longestValidParentheses(self, s: str) -> int:
        parenthesesStack = []
        stack = []
        for ch in s:
            if ch == '(':
                parenthesesStack.append(ch)
                stack.append(0)
                continue
            if len(parenthesesStack) > 0 and parenthesesStack[-1] == '(':
                parenthesesStack.pop()
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == 0:
                        stack[i] += 1
                        break
                while len(stack) > 1 and stack[-2] > 0:
                    last = stack.pop()
                    stack[-1] += last
            else:
                stack.append(0)
        return max(stack) * 2 if len(stack) > 0 else 0