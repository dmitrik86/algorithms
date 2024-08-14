class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        result = []
        def createExpressions(idx, expression, current):
            if n == idx:
                if eval(expression) == target:
                    result.append(expression)
                return
            signs = ['+', '-', '*']
            if current != 0:
                createExpressions(idx + 1, expression + num[idx], int(num[idx]) + (current * 10 if current != None else 0))
            if expression == '':
                return
            for sign in signs:
                createExpressions(idx + 1, expression + sign + num[idx], int(num[idx]))
        createExpressions(0, '', None)
        return result