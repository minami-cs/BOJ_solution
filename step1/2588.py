# 세 자리 수 2개 받기 a는 숫자, b는 문자열로 받기
# b 문자열을 숫자로 반환
# 숫자로 반환한 b 문자열을 a랑 하나씩 곱하기 해서 출력
# a*b 출력
a = int(input())
b = input()

b0 = int(b[0])
b1 = int(b[1])
b2 = int(b[2])

bb = int(b)

print(a*b2)
print(a*b1)
print(a*b0)
print(a*bb)