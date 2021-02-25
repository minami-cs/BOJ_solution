a = int(input())
b = int(input())
c = int(input())
r = list(str(a*b*c))
for i in range(10):
    print(r.count(str(i)))

# count함수는 문자열에 쓰이고 특정 문자 갯수를 세어준다.