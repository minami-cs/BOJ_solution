n = int(input())

v = 0
while n >= 0:
    if n % 5 == 0:
        print(v + (n // 5))
        break
    n -= 3
    v += 1
else:
    print(-1)
