def isPalinddrome(st):
    l = len(st)
    for i in range(l):
        if s[i] != s[l - i - 1]:
            return False
    return True


s = input()

print(isPalinddrome(s))


"""

RACECAR
True

"""