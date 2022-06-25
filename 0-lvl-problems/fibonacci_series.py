n = int(input())

fibo_series = 0
fibo_list = []
for i in range(n):
    if i <= 1:
        fibo_series += i 
        fibo_list.append(fibo_series)
    else:
        fibo_series = fibo_list[-1] + fibo_list[-2]
        fibo_list.append(fibo_series)

print(*fibo_list)
