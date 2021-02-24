t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print('Case #%s: %s + %s = %s'%(i+1,a,b,a+b))

#각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.