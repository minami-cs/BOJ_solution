c = int(input())

for i in range(c):
    a = list(map(int, input().split()))
    avg = (sum(a[1:]))/a[0]
    cnt = 0
    for j in a[1:]:
        if j > avg:
            cnt += 1
        s = cnt/a[0]*100
    print(f'{s:.3f}%')


# vs code에서는 멀쩡히 돌아가는데 자꾸 백준에서는 런타임에러가 났다. 변수를 몇 개 더 사용했는데 그래서 그런가...? typeerror가 계속 났다...
# 알고리즘 자체는 맞게 짰는데 자꾸 왜 그런 에러가 나는지 모르겠어서 다른 블로그 참고 후 변수를 몇 개 삭제하고 코드를 줄이니 드디어 정답이라고 나왔따.
# 참고: https://ooyoung.tistory.com/62