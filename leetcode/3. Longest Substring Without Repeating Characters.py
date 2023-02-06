class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        res = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub = sub[1:]
            sub += s[r]
            res = max(res, len(sub))
        return res
