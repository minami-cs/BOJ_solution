n = int(input())

for i in range(n):
    s = input()
    sum = 0
    cnt = 0
    for j in s:
        if j == 'O':
            cnt += 1
        else:
            cnt = 0
        sum += cnt
    print(sum)


# 참고: https://deokkk9.tistory.com/7
# 입력받은 문자열도 하나씩 비교 및 카운팅 가능