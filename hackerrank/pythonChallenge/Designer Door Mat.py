def oddadd(num):
    return num + 2


def oddminus(num):
    return num - 2


n, m = map(int, input().split())
pr = 1

for i in range(1, n + 1):
    pat = ".|." * pr
    design = ""
    l = len(pat)
    dummy = (m - l) // 2
    if i < n // 2:
        design = ("-" * dummy) + pat + ("-" * dummy)
        pr = oddadd(pr)
    elif (i) == (n // 2) + 1:
        design = ("-" * ((m // 2) - 3)) + "WELCOME" + ("-" * ((m // 2) - 3))
        pr = oddadd(pr)
    else:
        design = ("-" * dummy) + pat + ("-" * dummy)
        pr = oddminus(pr)

    print(design)
