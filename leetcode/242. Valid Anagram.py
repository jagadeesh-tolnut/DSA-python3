class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        if len(s) == len(t):
            for i in range(len(s)):
                a[s[i]] = a.get(s[i],0) + 1
                b[t[i]] = b.get(t[i],0) + 1
            if a == b:
                return True
            else:
                return False
        else:
            return False



'''
########### Solution 2 ###############

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = Counter(s)
        b = Counter(t)
        if a == b:
            return True
        else:
            return False


'''