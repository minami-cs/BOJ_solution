a = []
for i in range(10):
    a.append((int(input()))%42)
b = set(a)
print(len(b))


# set은 집합 자료형을 생성할 수 있는데 순서가 없고 중복을 허용하지 않는다.