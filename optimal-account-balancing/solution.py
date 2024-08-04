class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        n = 0
        for person1, person2, amount in transactions:
            n = max(n, person1, person2)
        balance = [0] * (n + 1)
        for person1, person2, amount in transactions:
            balance[person1] -= amount
            balance[person2] += amount
        personsWithNegativeBalance = []
        personsWithPositiveBalance = []
        for person in range(n + 1):
            if balance[person] < 0:
                personsWithNegativeBalance.append(person)
            if balance[person] > 0:
                personsWithPositiveBalance.append(person)
        result = float('inf')
        def backtrack(positiveIdx, numberOfTransactions):
            nonlocal result
            if numberOfTransactions > result:
                return
            if positiveIdx == len(personsWithPositiveBalance):
                result = min(result, numberOfTransactions)
                return
            personWithPositiveBalance = personsWithPositiveBalance[positiveIdx]
            for personWithnegativeBalance in personsWithNegativeBalance:
                if balance[personWithnegativeBalance] >= 0:
                    continue
                negativeBalance = balance[personWithnegativeBalance]
                positiveBalance = balance[personWithPositiveBalance]
                if positiveBalance + negativeBalance == 0:
                    balance[personWithnegativeBalance] = 0
                    balance[personWithPositiveBalance] = 0
                    backtrack(positiveIdx + 1, numberOfTransactions + 1)
                elif positiveBalance + negativeBalance < 0:
                    balance[personWithPositiveBalance] = 0
                    balance[personWithnegativeBalance] += positiveBalance
                    backtrack(positiveIdx + 1, numberOfTransactions + 1)
                elif positiveBalance + negativeBalance > 0:
                    balance[personWithnegativeBalance] = 0
                    balance[personWithPositiveBalance] += negativeBalance
                    backtrack(positiveIdx, numberOfTransactions + 1)
                balance[personWithnegativeBalance] = negativeBalance
                balance[personWithPositiveBalance] = positiveBalance
        backtrack(0, 0)
        return result