t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    temp = [j for j in range(1, n+1)]
    for f in range(1, k+1):
        for s in range(1, n):
            temp[s] += temp[s-1]
    print(max(temp))
