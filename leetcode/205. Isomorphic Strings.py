class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm1 = {}
        hm2 = {}
        for i in range(len(s)):
            hm1[s[i]] = t[i]
            hm2[t[i]] = s[i]

        for i in range(len(s)):
            if hm1[s[i]] != t[i] or hm2[t[i]] != s[i]:
                return False
        return True

