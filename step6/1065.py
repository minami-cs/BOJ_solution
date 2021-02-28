n = int(input())
cnt = 0

for i in range(1, n+1):
    temp = list(map(int, str(i)))
    if i < 100:
        cnt += 1
    elif temp[0]-temp[1] == temp[1]-temp[2]:
        cnt += 1
print(cnt)