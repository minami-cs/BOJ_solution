# 에라토스테네스의 체를 사용하자
m, n = map(int, input().split())
temp = []

for i in range(m, n+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j

for k in temp:
    print(k)
