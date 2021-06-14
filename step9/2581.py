# 소수
# 한 자리수: 2, 3, 5, 7
# 두 자리수 이상은 1의 자릿수가 1, 3, 7, 9

m = int(input())
n = int(input())
temp = []
for i in range(m, n+1):
    if i > 1:
        temp.append(i)
        for j in range(2, i):
            if i % j == 0:
                temp.remove(temp[temp.index(i)])
                break
if len(temp) < 1:
    print(-1)
else:
    print(sum(temp))
    print(min(temp))
