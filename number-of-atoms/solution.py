class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parseFormula(formula):
            n = len(formula)
            previous = ''
            cnt = 0
            elements = defaultdict(int)
            i = 0
            while i < n:
                if formula[i].isnumeric():
                    if cnt == 0:
                        cnt = int(formula[i])
                    else:
                        cnt = cnt * 10 + int(formula[i])
                    i += 1
                    continue
                if ord('A') <= ord(formula[i]) <= ord('Z'):
                    if previous:
                        elements[previous] += cnt if cnt > 0 else 1
                    previous = formula[i]
                    cnt = 0
                    i += 1
                    continue
                if ord('a') <= ord(formula[i]) <= ord('z'):
                    previous += formula[i]
                    i += 1
                    continue
                if formula[i] == '(':
                    cntOpened = 1
                    j = i + 1
                    while cntOpened > 0:
                        if formula[j] == '(':
                            cntOpened += 1
                        if formula[j] == ')':
                            cntOpened -= 1
                        j += 1
                    k = j
                    while k < n and formula[k].isnumeric():
                        k += 1
                    subElements = parseFormula(formula[i + 1:j - 1])
                    mult = int(formula[j:k]) if k > j else 1
                    for el, val in subElements.items():
                        elements[el] += (val if val > 0 else 1) * mult
                    i = k
            if previous:
                elements[previous] += cnt if cnt > 0 else 1
            return elements
        elements = parseFormula(formula)
        elementsName = sorted(elements.keys())
        result = []
        for name in elementsName:
            result.append(name)
            if elements[name] > 1:
                result.append(str(elements[name]))
        return ''.join(result)