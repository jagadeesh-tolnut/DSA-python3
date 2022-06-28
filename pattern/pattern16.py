n = int(input())
pascal_triangle = []

for i in range(n):
    if i == 0:
        pascal_triangle.append([1])
    elif i == 1:
        pascal_triangle.append([1,1])
    
    else:
        for j in range(n):
            app_list = [1]
            for k in range(1,len(pascal_triangle[-1])):
                app_list.append(pascal_triangle[-1][k-1]+pascal_triangle[-1][k])
            app_list.append(1)
        pascal_triangle.append(app_list)

for row in range(n):
    print(" "*(n-row), end="")
    print(*pascal_triangle[row])

            
