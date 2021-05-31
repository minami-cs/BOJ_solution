n = int(input())

for i in range(n):
    w = input()
    # range(len(w))이면 w.find(w[j-1])에서 w[-1]이 되므로 range(1, len(w))로 해주자.
    for j in range(1, len(w)):
        if w.find(w[j-1]) > w.find(w[j]):
            n -= 1
            # 그룹단어가 아닌 경우 계속 검사하지 않고 다음 단어를 검사하도록 넘어가게 break를 걸어주자
            break

print(n)
