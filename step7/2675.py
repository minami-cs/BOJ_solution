t = int(input())
for i in range(t):
    r, s = input().split()
    s2 = ''
    for j in s:
        s2 += j * int(r)
    print(s2)
