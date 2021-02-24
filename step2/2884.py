h, m = input().split()
h = int(h)
m = int(m)

if m < 45:
    h = h-1
    m = 60 - 45 + m
    if h < 0:
        h = 23
    print(h, m)
else:
    print(h, m-45)

# https://tre2man.tistory.com/121 참고