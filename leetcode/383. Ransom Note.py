class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = ransomNote
        m = magazine
        for i in r:
            if i in m:
                m = m.replace(i, "", 1)
            else:
                return False
        return True

