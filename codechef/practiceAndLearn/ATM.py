w, b = map(float, input().split())
if w % 5 == 0 and w + 0.50 <= b:
    print("{:.2f}".format(b - w - 0.50))
else:
    print("{:.2f}".format(b))
