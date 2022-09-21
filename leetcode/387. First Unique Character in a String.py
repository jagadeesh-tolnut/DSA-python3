class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            if not (s[i] in s[i + 1:]) and not (s[i] in s[:i]):
                return i
        return -1
