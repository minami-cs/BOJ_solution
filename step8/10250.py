t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    a = n % h
    b = n // h
    if a == 0:
        print(h*100+b)
    else:
        print(a*100+b+1)
