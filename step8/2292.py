n = int(input())

#1, 7, 19, 37, 61
cnt = 1
six = 6
num = 1
if n == 1:
    print(1)
else:
    while True:
        cnt += six
        six += 6
        num += 1
        if n <= cnt:
            print(num)
            break
