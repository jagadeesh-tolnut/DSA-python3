n = int(input())
res = []
grade = []
for i in range(n):
    name = input()
    mark = float(input())
    res.append([name, mark])
    grade.append(mark)
grade = sorted(set(grade))
m = grade[1]
name = []
for val in res:
    if m == val[1]:
        name.append(val[0])
name.sort()
for nm in name:
    print(nm)

