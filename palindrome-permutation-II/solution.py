class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        n = len(s)
        if n == 0:
            return []
        counter = defaultdict(int)
        for lt in s:
            counter[lt] += 1
        numberOfOdd = 0
        oddLetter = ''
        for lt in counter:
            if counter[lt] % 2 > 0:
                numberOfOdd += 1
                oddLetter = lt
        if numberOfOdd > 1:
            return []
        if numberOfOdd == 0:
            current = ''
        else:
            current = oddLetter
            counter[oddLetter] -= 1
        result = []
        def permutate(current, counter):
            letterExists = False
            for lt in counter:
                if counter[lt] == 0:
                    continue
                letterExists = True
                counter[lt] -= 2
                permutate(lt + current + lt, counter)
                counter[lt] += 2
            if letterExists == False:
                result.append(current)
        permutate(current, counter)
        return result