# 에라토스테네스의 체를 사용하자
# 시간초과
# m, n = map(int, input().split())

# for i in range(m, n+1):
#     if i == 2:
#         print(i)
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         elif j == i-1:
#             print(i)

def isPrime(num):
    if num == 1:
        return False
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


m, n = map(int, input().split())
for k in range(m, n+1):
    if isPrime(k):
        print(k)
