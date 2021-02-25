n = int(input())
a = list(map(int,input().split()))
m = max(a)

for i in range(n):
    a[i] = a[i]/m*100
r = sum(a)/n
print('%.2f'%r)

# 참고: https://jeongmin-lee.tistory.com/44