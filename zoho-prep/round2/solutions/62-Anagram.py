def isAnagram(st1,st2):
    return True if sorted(st1) == sorted(st2) else False


l = list(map(str,input().split()))
word = input()

for i in l:
    if isAnagram(i,word):
        print(i,end=" ")

"""
i/p
catch got tiger mat eat Pat tap tea
ate

o/p
eat tea

"""