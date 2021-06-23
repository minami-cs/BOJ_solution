# 10: 5,5 [2 3 5 7]

def isPrime():
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [False, False] + [True] * 10000
    # num의 최대 약수가 sqrt(num) 이하이므로 i=sqrt(num)까지 검사
    for i in range(2, 101):
        if sieve[i] == True:            # i가 소수인 경우
            for j in range(i+i, 10001, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    t = int(input())
    for k in range(t):
        n = int(input())
        a = n // 2
        b = a
        while a > 0:
            if sieve[a] and sieve[b]:
                print(a, b)
                break
            else:
                a -= 1
                b += 1


isPrime()

# 참조: https://deokkk9.tistory.com/20, https://yoonsang-it.tistory.com/31
