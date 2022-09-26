class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        n = len(s)
        if n == 0:
            return True
        for i in t:
            if s[p] == i:
                p+=1
            if p == n:
                return True
        return False