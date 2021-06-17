def isPrime(num):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * num
    # num의 최대 약수가 sqrt(num) 이하이므로 i=sqrt(num)까지 검사
    for i in range(2, int(num**0.5)+1):
        if sieve[i] == True:            # i가 소수인 경우
            for j in range(i+i, num, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False
    # 소수 목록 산출
    return [i for i in range(2, num) if sieve[i] == True]

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(len([i for i in isPrime(2*n+1) if i > n]))