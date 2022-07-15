n = int(input())
ALT = int(input())
APPS = list(map(int,input().split()))

recent = APPS.pop(ALT-1)
APPS.insert(0,recent)

print(*APPS)