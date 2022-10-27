class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        value = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

        for i, v in enumerate(s[:-1]):
            if value[v] >= value[s[i + 1]]:
                num += value[v]
            else:
                num -= value[v]

        num += value[s[-1]]

        return num