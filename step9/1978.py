# 소수
# 한 자리수: 2, 3, 5, 7
# 두 자리수 이상은 1의 자릿수가 1, 3, 7, 9

n = int(input())
nums = map(int, input().split())
sum = 0
for i in nums:
    temp = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                temp += 1
        if temp == 0:
            sum += 1
print(sum)
