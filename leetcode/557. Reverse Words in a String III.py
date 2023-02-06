class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        final = ""
        for i in s:
            if i == " ":
                final += temp[::-1] + " "
                temp = ""
            else:
                temp += i

        final += temp[::-1]

        return final