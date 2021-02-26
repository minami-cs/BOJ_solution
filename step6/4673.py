n = list(range(1, 10001))
d = []

for i in n:
    for j in str(i):
        i += int(j)
    if (i < 10001):
        d.append(i)
for k in range(1, 10001):
    if k in d:
        pass
    else:
        print(k)

# list 활용은 생각해냈는데 문자열로 슬라이싱해서 더해야 하나 했다가 어떻게 해야 할지 모르겠어서 결국 검색 후 참고를 했다.
# 참고1: https://ooyoung.tistory.com/64
# 참고2: https://claude-u.tistory.com/33